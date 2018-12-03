import objects
def make_lists(data):
    day_strings = data.replace("Mon", "splitplaceholder").replace("Tue", "splitplaceholder").replace("Wed", "splitplaceholder").replace("Thu", "splitplaceholder").replace("Fri", "splitplaceholder").split("splitplaceholder")

    mon, tue, wed, thu, fri = day_strings[1], day_strings[2], day_strings[3], day_strings[4], day_strings[5]
    return [mon, tue, wed, thu, fri]

def process_day(s, day): # PASS THE DAY NAME SO THE OBJECTS CAN BE ASSIGNED THE DAY JUST IN CASE
    s = s.strip()
    keys = s.split("\n")
    keys = keys[2:] # discard empty slots at 8:00 and 8:30
    output_list = []
    i = 0

    while i < len(keys):
        start_strings = ["Prac.", "Lec.", "Tut.", "emptySlot"]
        if keys[i] == "emptySlot":
            output_list.append(None)
            i += 1
        else:
            if keys[i+4][0].isdigit():
                tmp_type = keys[i]
                tmp_loc = keys[i+1]
                tmp_name = keys[i+2]
                tmp_code = keys[i+3]
                tmp_weeks = keys[i+4]

                output_list.append(objects.Timeslot(tmp_type, tmp_loc, tmp_name, tmp_code, tmp_weeks, day))
                i += 5
            else:
                tmp_type = keys[i]
                tmp_loc = keys[i+1]
                # tmp_lecturer = keys[i+2]
                tmp_name = keys[i+3]
                tmp_code = keys[i+4]
                tmp_weeks = keys[i+5]
                output_list.append(objects.Timeslot(tmp_type, tmp_loc, tmp_name, tmp_code, tmp_weeks, day))
                i += 6

    return output_list

def make_lists_days(l):
    d = {
    "monday" : process_day(l[0], "Mon"),
    "tuesday" : process_day(l[1], "Tue"),
    "wednesday" : process_day(l[2], "Wed"),
    "thursday" : process_day(l[3], "Thu"),
    "friday" : process_day(l[4], "Fri")
    }

    return d


# TODO: account for spaces in module names
