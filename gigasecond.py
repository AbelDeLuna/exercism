import datetime

def add_gigasecond(birth_date):
    delta = 10**9
    return birth_date + datetime.timedelta(0,delta) 

