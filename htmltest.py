import html2text
import urllib3
import requests
import ssl
import re
from bs4 import BeautifulSoup
from cleaner import cleanup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def url_assembler():
    print("Enter program code (Defaults to CASE)")
    code = input()
    print("Enter year (Defaults to 2)")
    year = input()
    print("Enter semester (Defaults to 1)")
    sem = input()

    print_from_url(code, year, sem)


def timetable_getter(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    return mystr


def main():
    url_assembler()


def print_from_url(code="CASE", year="2", sem="2"):
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    text_maker.bypass_tables = False
    if sem == "1":
        url = "https://www101.dcu.ie/timetables/feed.php?prog={}&per={}&week1={}&week2={}&hour=1-20&template=student".format(code, year, "1", "12")
    elif sem == "2":
        url = "https://www101.dcu.ie/timetables/feed.php?prog={}&per={}&week1={}&week2={}&hour=1-20&template=student".format(code, year, "1", "12")
    else:
        url = "https://www101.dcu.ie/timetables/feed.php?prog=CASE&per=2&week1=1&week2=12&hour=1-20&template=student"
    # TODO put in weeks for semester 2

    html = requests.get(url, verify=False)
    html = BeautifulSoup(html.content, 'html.parser')
    html = str(html)
    text = text_maker.handle(html)
    text = cleanup(text)
    print(text)
    print_to_file(text)


def print_to_file(s):
    with open("output.txt", "w") as text_file:
        print(s, file=text_file)


if __name__ == '__main__':
    main()
