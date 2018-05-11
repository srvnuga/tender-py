import time
import random
from time import gmtime

class DateUtils:
    DATE_FORMAT = '%m/%d/%Y %I:%M %p'

    @staticmethod
    def generate_random_date(start, end):

        stime = time.mktime(time.strptime(start, DateUtils.DATE_FORMAT))
        etime = time.mktime(time.strptime(end, DateUtils.DATE_FORMAT))
        prop = random.random()
        ptime = stime + prop * (etime - stime)

        return time.strftime(DateUtils.DATE_FORMAT, time.localtime(ptime))


    @staticmethod
    def is_target_before_now (target_date):
        bdate = time.mktime(gmtime())
        tdate = time.mktime(time.strptime(target_date, DateUtils.DATE_FORMAT))
        return bdate > tdate



