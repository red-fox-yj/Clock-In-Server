import csv

temp_list = [
    "刘薇",
    "高志远",
    "陈焱燚",
    "王鹏",
    "陈文婷",
    "张宁馨",
    "乔萌龙",
    "金宁",
    "杜蕾",
    "王瑜",
    "张珂",
    "吴佳蕾",
    "刘千嘉",
    "舒畅",
    "董涵",
    "高梦娟",
    "朱夏晶",
    "韩祎玮",
    "田宇",
    "郑文超",
    "王振华",
    "王茹斯",
    "杨捷",
]


def _WriteToCsv(names: list):
    """将名单写入CSV"""
    with open(
        "names.csv",
        "w",
        newline="",
        encoding="UTF8",
    ) as csvfile:
        writer = csv.writer(csvfile)
        for row in names:
            writer.writerow([row])


def _ReadNames():
    """将名单写入CSV"""
    with open(
        "names.csv",
        "r",
        newline="",
        encoding="UTF8",
    ) as csvfile:
        temp = []
        reader = csv.reader(csvfile)
        for row in reader:
            temp.append(row[0])
    return temp


def _modify(names_str: str):
    """"""
    _WriteToCsv(names_str.split(","))


print("，".join(_ReadNames()))
