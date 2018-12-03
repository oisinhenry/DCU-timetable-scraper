import html2text
import urllib3
import requests
import ssl
import re
from bs4 import BeautifulSoup
from cleaner import cleanup
from objects import Timeslot
from dtsparser import make_lists,process_day,make_lists_days
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # filed under "don't do this"

# this function basically exists for testing purposes right now. whenever we start exporting
# to standard calendar formats it'll probably be changed to command line params
def url_assembler():
    print("Enter program code (Defaults to CASE)")
    code = input()
    print("Enter year (Defaults to 2)")
    year = input()
    print("Enter semester (Defaults to 1)")
    sem = input()
    print_from_url(code, year, sem)


def timetable_getter(url): # pulls the raw HTML from the specified timetable URL
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    return mystr

def weeks_parser(weeks):
    if len(weeks) == 1:
        return [int(weeks)]
    elif weeks == "1-12":
        return [i for i in range(1,13)] # TODO: finish this


def main(): # another testing placeholder for now.
    url_assembler()


def print_from_url(code="CASE", year="2", sem="2"): # url assembler. this will exist in some form in the final build.
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    text_maker.bypass_tables = False
    if sem == "1":
        url = "https://www101.dcu.ie/timetables/feed.php?prog={}&per={}&week1={}&week2={}&hour=1-20&template=student".format(code, year, "1", "12")
    elif sem == "2":
        url = "https://www101.dcu.ie/timetables/feed.php?prog={}&per={}&week1={}&week2={}&hour=1-20&template=student".format(code, year, "1", "12")
    else:
        url = "https://www101.dcu.ie/timetables/feed.php?prog=CASE&per=2&week1=1&week2=12&hour=1-20&template=student"
    # TODO: put in weeks for semester 2
    # TESTING LINE ONLY (for when the timetables are offline)
    url = "http://oisin.website/timetable/"
    # TESTING LINE ONLY
    html = requests.get(url, verify=False)
    html = BeautifulSoup(html.content, 'html.parser')
    html = str(html)
    text = text_maker.handle(html)
    text = cleanup(text)
    # print(text)
    # print_to_file(text)
    list_day_strings = make_lists(text)

    days = make_lists_days(list_day_strings)
    output_string = ""
    for key in days:
        output_string +="\n\n\nSTART DAY"+ key+":\n------"
        for item in days[key]:
            output_string += str(item) + "\n"

    with open("output_all_days.txt", "w") as outputdays:
        print(output_string, file=outputdays)


def print_to_file(s): # this isn't really used except for testing
    with open("output.txt", "w") as text_file:
        print(s, file=text_file)


def table_getter(data):
    soup = BeautifulSoup(data)
    raw_html = ""
    for table in soup.find_all("td"):
        raw_html += str(table)


def rowspan_getter(tables):
    keys = tables.split("td rowspan")
    keys = keys[1:6]
    values = []
    for key in keys:
        values.append(int(key[2]))

    return values

def colspan_getter(tables):
    keys = tables.split("colspan")
    keys = keys[21:]
    values = []
    for key in keys:
        values.append(int(key[2]))

    return values



if __name__ == '__main__':
    main()
