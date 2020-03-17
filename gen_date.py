def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for minut in range(60):
        yield minut

def gen_hours():
    for hour in range(24):
        yield hour

def gen_time():
    for hour in gen_hours():
        for minut in gen_minutes():
            for sec in gen_secs():
                yield "{:02d}:{:02d}:{:02d}".format(hour, minut, sec)

def gen_years(start=2019):
    for year in range(start, 2150):
        yield year


def gen_months():
    for month in range(1, 13):
        yield month

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
def gen_days(month):
    leap_year = is_leap_year(month)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_of_month = 31
    elif month in [4, 6, 9, 11]:
        days_of_month = 30
    elif leap_year:
        days_of_month = 29
    else:
        days_of_month = 28
    for day in range(1, days_of_month +1):
        yield day


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month):
                for time in gen_time():
                    yield "{:02d}/{:02d}/{:04d}".format(day, month, year) +" " + time




for index ,gt in enumerate(gen_date()):
    if index % 1000000 == 0 and index != 0:
        print(gt)







































# for gt in gen_time():
#     print(gt)