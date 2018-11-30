import re
def cleanup(s):
    s = s.replace("|", "")
    s = s.replace("---", "")
    s = s.replace("![]", "")
    s = s.replace("(http://www.dcu.ie/images/space.gif)", "emptySlot\n")
    s = re.sub(r"\<(.*?)\>", "", s)
    s = s.split("17:30")[1]
    s = s.split("Sat")[0]
    s = s.replace(", ", ",")
    s = s.replace(",\n", "")
    s = s.replace("  ", "\n")
    s = s.replace("   ", "\n")
    s = s.replace("\n ", "\n")
    s = re.sub(r"\n+", "\n\n", s)
    s = re.sub(r"\[(.*?)\n", "", s)
    return s
