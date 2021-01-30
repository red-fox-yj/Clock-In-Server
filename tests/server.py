import asyncio
import websockets
import time


async def echo(websocket, path):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        await websocket.send(message)

        while True:
            await asyncio.sleep(1)
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            await websocket.send(t)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, "localhost", 8000)
)
asyncio.get_event_loop().run_forever()
