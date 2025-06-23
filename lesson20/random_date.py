
import random

import time

def randomdategenerator(startdate,enddate):
    print("printing random date between", {startdate},  "and", {enddate})
    random_generator = random.random()
    date_format = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startdate,date_format))
    endtime = time.mktime(time.strptime(enddate,date_format))
    random_time = starttime + random_generator * (endtime - starttime)
    random_date = time.strftime(date_format, time.localtime(random_time))
    return random_date

print("the random date is", randomdategenerator("12/12/2025", "12/12/2070"))
