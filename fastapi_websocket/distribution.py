import csv


def _search(checked_names_str: str):
    """查询"""
    unchecked_names_list = []
    all_names_list = _ReadNames()
    for item in all_names_list:
        if item not in checked_names_str:
            unchecked_names_list.append(item)

    return "@" + "@".join(unchecked_names_list)


def _read():
    """读取名单"""
    return "，".join(_ReadNames())


def _modify(names_str: str):
    """"""
    _WriteToCsv(names_str.split("，"))


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
