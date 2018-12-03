# to be made into a real func and added to main
# this function gets the timeslot widths (i.e. the duration of each lecture)
# and simply returns them in a list.
# 
f1 = open("output.txt", "r")

s = f1.read()

keys = s.split("colspan")

keys = keys[21:]
values = []
for key in keys:
    values.append(int(key[2]))


newvalues = [n//2 for n in values]


print(newvalues)
