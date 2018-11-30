class Timeslot(object):
    def __init__(self, day, time, slot_type, location, module_name, module_code, weeks):
        self.day = day
        self.time = time
        self.slot_type = slot_type
        self.location = location
        self.module_name = module_name
        self.weeks = weeks

    def __str__(self):
        if self.slot_type == "empty":
            return None
        else:
            s = "Class type: {}\nDay: {}\nLocation: {}\nModule: {}\nWeeks: {}".format(self.day, self.location, self.module_code+self.module_name, self.weeks)
