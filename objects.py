class Timeslot(object):
    def __init__(self, slot_type, location, module_name, module_code, weeks, day=None, time=None):
# TIME INITS AS 0 because it's not worried about in our first pass with dtsparser.
# instead 5 lists of timeslot objects are assembled, one for each day. None type entries
# represent empty slots. each day is in order by the time they occur.
# TODO: write another function to go through THESE lists and cross reference them against some dictionary assigning
# actual times to each one.
        self.day = day
        self.time = time
        self.slot_type = slot_type
        self.location = location
        self.module_name = module_name
        self.weeks = weeks

    def __str__(self):
        # if self.slot_type == "empty":
        #     return None

        return "-----\nClass type: {}\nDay: {}\nLocation: {}\nModule: {}\nWeeks: {}".format(self.slot_type, self.day, self.location, self.module_name, self.weeks)


# TODO: do away with slot_type "empty" and just use None objects for empty slots. Timeslot objects will always be populated this way
