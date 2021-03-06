import logging
from datetime import date, timedelta, datetime

def get_dates(m, y):
    print("Getting a list of dates for", m, "-", y)
    ndays = (date(y, m + 1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1
    print("")
    return [(d1 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]

