# DCU Timetable Scraper

WIP timetable scraper for DCU. Written in Python 3.


## TODO:

* ~~Structure text data parsed from HTML file.~~

* ~~Implement timeslot objects.~~ (this isn't totally finished yet).

* Implement a function to iterate through all the text data and create Timeslot objects. (currently working in the testing environment)

* Implement a function to do another pass over the raw HTML and extract the width of each populated column (i.e. the duration of each lecture). Output to some list. (currently working in the testing environment)

* Add a duration attribute to the Timeslot object and cross reference with aforementioned list.

* Store those Timeslot objects in order by day and then by time.

* ~~Implement methods to query and print the list(?) of Timeslot objects.~~
I probably won't do this. The print method is already implemented and querying is fairly redundant.

* Output those objects to CSV!


## Long term goals:

* Output to some (standardized) format readable by humans (not just python command line).

* Package as a web app (React?) and implement Google Calendar export functionality.

* My buddy Conor is currently working on the frontend [here](https://github.com/LemonUnderscore/DCU-Timetable-Webapp). Hoping to meet in the middle and end up with some kind of functional product.


## Dependencies

[HTML2Text](https://pypi.org/project/html2text/)

[BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```
pip install html2text

pip install BeautifulSoup4
```
