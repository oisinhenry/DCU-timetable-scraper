from dtsparser import make_lists, process_day
import objects

with open("output.txt", "r") as f1:
    s = f1.read()

day = make_lists(s)
monday = day[0]

daytest = process_day(monday, "Mon")

for line in daytest:
    print(line)
