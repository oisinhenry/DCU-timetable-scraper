# this gets the rowspan attr of each day.
# to be cross referenced later with all the timeslot objects
f1 = open("output.txt", "r")

s = f1.read()

keys = s.split("td rowspan")

keys = keys[1:6]
values = []
for key in keys:
    values.append(int(key[2]))

print(values)
# newvalues = [n//2 for n in values]
#
#
# print(newvalues)
