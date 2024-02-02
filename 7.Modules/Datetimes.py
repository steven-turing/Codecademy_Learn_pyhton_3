# 1.Datetime module
from datetime import datetime
# Create a date using -year, month, day as argument
birthday = datetime(1994, 2, 15, 4, 25, 12)

print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.weekday())

# Create a date using datetime.now()
print(datetime.now())
print(datetime(2024, 2, 2) - datetime(1993, 1, 3))
print(datetime.now() - datetime(1993, 1, 3))

# 2.string p time function: strptime()
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date.month)

# 3.string p time function: srtftime()
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)

