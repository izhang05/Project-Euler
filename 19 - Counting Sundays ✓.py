"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""
year = 1901
day = 1
day_of_week = 2
solution = 0
while year < 2001:
	for month in range(1, 13):
		if day_of_week == 0:
			solution += 1
		if month == 4 or month == 6 or month == 9 or month == 11:
			days_in_month = 30
		elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
			days_in_month = 31
		elif month == 2:
			if year % 4 != 0:
				days_in_month = 28
			elif year % 100 == 0 and year % 400 != 0:
				days_in_month = 28
			else:
				days_in_month = 29
		day_of_week = (day_of_week+days_in_month)%7
	else:
		year += 1
print(solution)