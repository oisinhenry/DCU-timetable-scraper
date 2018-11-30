f1 = open("output.txt", "r")
s = f1.read()

s = s.replace("|", "")
s = s.replace("---", "")
s = s.replace("![]", "")
s = s.replace("(http://www.dcu.ie/images/space.gif)", "emptySlot\n")
# s = s.replace(" ", "\n")



print(s)


with open("replacetest.txt", "w") as file:
    print(s, file=file)
