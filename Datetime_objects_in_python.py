from datetime import date, datetime, timedelta

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

MONTH = 30.436875 * DAY  # Average days a month in solar calendar
YEAR = 365.2425 * DAY  # Solar calendar

duration = datetime(1969, 7, 21, 2, 53) - datetime(1961, 4, 12, 6, 7)

years, seconds = divmod(duration.total_seconds(), YEAR)
months, seconds = divmod(seconds, MONTH)
days, seconds = divmod(seconds, DAY)
hours, seconds = divmod(seconds, HOUR)
minutes, seconds = divmod(seconds, MINUTE)



result = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}

delta = datetime.now() - timedelta(days = 2)
print("2 days ago we have:", delta)

iso_format = datetime.now().isoformat()
print("Today's date in iso format", iso_format)


today_iso = date.today().isoformat()
print("Today's date in iso format 2: ", today_iso)


"""
String format time
"""

dt = datetime(1969, 7, 21, 2, 53)
date_string = dt.strftime('%Y-%m-%d')
date_string2 = dt.strftime('%d %m %Y')

print(dt)
print(date_string)
print(date_string2)


"""
string parse time - create datetime object from a given string
"""

date_string = "20 October, 2020"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


date_with_int = '07/21/69 02:53:00'
new_date = datetime.strptime(date_with_int, '%m/%d/%y %H:%M:%S')
print("New date:", new_date)