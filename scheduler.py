from datetime import datetime
from school_calendar import calendar, days
from time_quote_finder import find_time_quote
from quote_display_3 import display_quote
import time
# import schedule

# every day at 6 am, get the day
# pull the day's schedule from calendar - check
# set key times according to day's schedule
# every 60 seconds - check
# do the thing and display it
# at the end of the day, sleep until 6 am the next day
# set chronjob to run scheduler every day at 6?

def get_time():
    now = datetime.now()
    return now

def get_schedule(y,m,d):
    try:
        return days[calendar[y][m][d]]
    except KeyError:
        return False

def time_string(h,m):
    if len(str(m)) < 2:
        m = '0' + str(m)
    return f"{h}:{m}"


t = get_time()
sched = get_schedule(t.year,t.month,t.day)
# print(t.strftime('%A')) # day of the week
# print(t.strftime('%B')) # month of the year

end = list(sched.keys())[len(list(sched.keys()))-1]

# # testing
end_hour = 15 # set to whichever you want 0 - 23
end_minute = 0 # set to whichever you want 0 - 59
# end_hour = int(end[:end.find(':')])
# end_minute = int(end[end.find(':')+1:])

while end_hour - t.hour > 0 or end_minute - t.minute > 0: 
    t = get_time()
    # print(t)
    ts = time_string(t.hour,t.minute)
    wait = 60
    if ts in list(sched.keys()):
        to = sched[ts]
        to.update({
            'text': t.strftime('%A') + ', ' + t.strftime('%B') + ' ' + str(t.day) + ', ' + str(t.year) + ' ' + sched[ts]['text-time'],
        }) #works
        wait *= 5
    else:
        to = find_time_quote(ts)

    display_quote(to)
    # send to epd

    # sleep
    ms = (float(wait*1000000) - (t.second*1000000) - t.microsecond)/1000000
    time.sleep(ms)

print('Scheduler has ended for the day')

# perfect!