from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
import ast
from distribution import _search, _modify, _read

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://192.168.0.74:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse("welcome")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive()

        await websocket.send_json(_resolve_response(data["text"]))
        # await websocket.send_text(data["text"])
        # await websocket.send_text(_resolve_response(str(data)[39:-2]))
        # await websocket.send_text(_resolve_response(str(data)))


def _resolve_response(response: str):
    """分发消息"""
    response = list(response)
    while "\n" in response:
        response.remove("\n")
    response = "".join(response)
    # 字符串转json
    response = ast.literal_eval(response)
    if response["type"] == "search":
        temp = {"type": "search", "data": _search(response["data"])}
    elif response["type"] == "read":
        temp = {"type": "read", "data": _read()}
    else:
        _modify(response["data"])
        temp = {"type": "modify", "data": "修改成功"}
    return temp


uvicorn.run(app, host="0.0.0.0", port=8000)
