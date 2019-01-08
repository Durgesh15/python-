#leap year
month_days=[0,31,28,31,30,31,30,31,30,31,30]

def is_leap(year)
	return year%4==0 and(year%100!=0 or year%400==0)

	