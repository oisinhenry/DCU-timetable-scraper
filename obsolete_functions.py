def print_from_file():
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    text_maker.bypass_tables = False
    html = open("timetable.html")
    html = html.read()
    text = text_maker.handle(html)
    print(text)
    print_to_file(text)


def print_to_file(s):
    with open("output.txt", "w") as text_file:
        print(s, file=text_file)
