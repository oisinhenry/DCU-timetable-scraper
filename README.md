# DCU Timetable Scraper

I go to DCU. The timetables for the courses in DCU aren't very nice looking. The form to request your timetable isn't very nice looking either. The website that the timetables live on also has a tendency to go down for days at a time.

I wanted to resolve some of these issues with a timetable scraper, which I've been writing in Python 3. My hope is to eventually deploy this as a React web app which all students will be able to use to import their timetable to Google Calendar.


## TODO:

* ~~Structure text data parsed from HTML file.~~

* ~~Implement timeslot objects.~~ (this isn't totally finished yet).

* Implement a function to iterate through all the text data and create Timeslot objects. (currently working in the testing environment)

* Implement a function to do another pass over the raw HTML and extract the width of each populated column (i.e. the duration of each lecture). Output to some list. (currently working in the testing environment)

* Add a duration attribute to the Timeslot object and cross reference with aforementioned list.

* Store those Timeslot objects in order by day and then by time.

* ~~Implement methods to query and print the list(?) of Timeslot objects.~~
I probably won't do this. The print method is already implemented and querying is fairly redundant.

* Run a pass over the `weeks` attribute for each Timeslot object and normalize them. e.g. `2-4,6-7` becomes `[2,3,4,6,7]`.

* Output a completed timetable to CSV!


## Long term stuff:

* Package as a React web app and implement Google Calendar export functionality.

* My buddy Conor is currently working on the frontend [here](https://github.com/LemonUnderscore/DCU-Timetable-Webapp). Hoping to meet in the middle and end up with some kind of functional product.


## Dependencies

[HTML2Text](https://pypi.org/project/html2text/)

[BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```
pip install html2text

pip install BeautifulSoup4
```
