from bs4 import BeautifulSoup


def convertToJson():
    soup = BeautifulSoup(open("./1.htm",encoding="utf-8"), "html.parser")
