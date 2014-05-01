'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
months = {}
months[1] = 31
months[2] = 28
months[3] = 31
months[4] = 30
months[5] = 31
months[6] = 30
months[7] = 31
months[8] = 31
months[9] = 30
months[10] = 31
months[11] = 30
months[12] = 31

'''
Starts 1 Monday 1901 to 31 December 2000
'''
def sundays():
	dayCount = 365
	sundayCount = 0
	for year in xrange(1,101):
		for month in xrange(1,13):
			if month == 2 and year % 4 == 0:
				dayCount += 29
			else:
				dayCount += months[month]
			if (dayCount + 1) % 7 == 0:
				sundayCount += 1
	return sundayCount


def main():
	print sundays()

if __name__ == "__main__":
    main()