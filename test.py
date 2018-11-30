import re
import textwrap


f1 = open("output.txt", "r")
s = f1.read()

s = s.replace("|", "")
s = s.replace("---", "")
s = s.replace("![]", "")
s = s.replace("(http://www.dcu.ie/images/space.gif)", "emptySlot\n")

# s = s.replace(" ", "\n")
s = re.sub(r"\<(.*?)\>", "", s)
# s = re.sub(r".+?(?=8:00)", "", s)

s = s.split("17:30")[1]
s = s.split("Sat")[0]
s = s.replace(", ", ",")
s = s.replace(",\n", "")
s = s.replace("  ", "\n")
s = s.replace("   ", "\n")
s = s.replace("\n ", "\n")
s = re.sub(r"\n+", "\n\n", s)
s = re.sub(r"\[(.*?)\n", "", s)



print(s)


with open("replacetest.txt", "w") as file:
    print(s, file=file)
