# function to show total years, months and days
# first written 19 Dec 2008/last updated 23 Dec 2008

# history
# 01 Mar 2012: bug fixed
# 23 Dec 2008: function for the day added
#              arguments changed to year, month and day
# 21 Dec 2008: ported into python
# 19 Dec 2008: first draft in gawk

def modifiedint(number):
	if number < 0 and number != int(number):
		return int(number) - 1;
	else:
		return int(number);

def getnobenen(year):
	return year;

def getnobetsuki(year, month):
	return 12 * (year - 1) + month;

def getnobehi(year, month, day):

	lastyear = year - 1;
	daysuntillastyear = 365 * lastyear + int(lastyear / 4) - int(lastyear / 100) + int(lastyear / 400);

	## reference
	## Japan Coast Guard. Accessed 23 Dec 2008
	#p = month - 1;
	#q = modifiedint((month + 7) / 10);
	#y = modifiedint((year / 4) - modifiedint(year / 4) + 0.77);
	#s = modifiedint(p * 0.55 - 0.33);
	#tsuujitsu = 30 * p + q * (s - y) + p * (1 - q) + day;

	a = 1;
	tsuujitsu = 0;
	while a < month:
		if a in [1, 3, 5, 7, 8, 10, 12]:
			tsuujitsu += 31;
		elif a in [4, 6, 9, 11]:
			tsuujitsu += 30;
		else:
			tsuujitsu += 28;
		a += 1;

	if month < 3:
		pass;
	elif year % 400 == 0:
		tsuujitsu += 1;
	elif year % 100 == 0:
		pass;
	elif year % 4 == 0:
		tsuujitsu += 1;
	else:
		pass;
	tsuujitsu += day;

	return daysuntillastyear + tsuujitsu;

