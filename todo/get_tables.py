# this gets the tables to pass to get_timeslot_widths.
# needs to be edited to pull the html from the site instead of locally,
# and then added to main along with get_timeslot_widths.
from bs4 import BeautifulSoup

data = open("timetable.html")

soup = BeautifulSoup(data)
s = ""

for table in soup.find_all("td"):
    print(str(table))
    s += str(table)
    # for subtable in table.find_all("tr"):
    #     print(str(subtable))
    #     s += str(subtable)


with open("output.txt", "w") as file:
    print(s, file=file)
