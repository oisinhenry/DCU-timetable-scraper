import re
# this function is a bit quick and dirty but it gets the job done for a first
# pass on beautifying our data.
# TODO: make more efficient? maybe not neccessary.
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
    s = re.sub(r"\n+", "\n\n", s) # double newline is purely for readability by humans
    s = re.sub(r"\((.*?)\n", "", s)
    s = re.sub(r"\[(.*?)\n", "", s)
    s = s.replace("\n\n", "\n")

    # lines = s.split("\n")
    # lines_new = []
    # for line in lines:
    #     if line:
    #         if line[0].isdigit():
    #             line = "\n"+line
    # s = "".join(s)
    return s

# TODO: normalise the newlines between each element (!!!)
