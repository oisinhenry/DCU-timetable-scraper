# DCU Timetable Scraper

I go to DCU. The timetables for the courses in DCU aren't very nice looking. The form to request your timetable isn't very nice looking either. The website that the timetables live on also has a tendency to go down for days at a time.

I wanted to resolve some of these issues with a timetable scraper, which I've been writing in Python 3. My hope is to eventually deploy this as a React web app which all students will be able to use to import their timetable to Google Calendar.


## TODO:

* ~~Structure text data parsed from HTML file.~~

* ~~Implement timeslot objects.~~

* ~~Implement a function to iterate through all the text data and create Timeslot objects.~~

* ~~Implement a function to do another pass over the raw HTML and extract the width of each populated column (i.e. the duration of each lecture). Output to some list.~~
This is working at the moment but needs to be called in main and tested some more.

* ~~Add a duration attribute to the Timeslot object~~ and cross reference with aforementioned list. This is very important. Need to write that cross reference function.

* ~~Store those Timeslot objects in order by day and then by time.~~ They currently sit in a dictionary with `Day : ListOfTimeslots` but they need to be revisited - durations to be added and weeks to be normalized.

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
