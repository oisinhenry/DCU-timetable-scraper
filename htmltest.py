import html2text
text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
text_maker.bypass_tables = False
html = open("timetable.html")
html = html.read()
text = text_maker.handle(html)
print(text)

with open("output.txt", "w") as text_file:
    print(text, file=text_file)
