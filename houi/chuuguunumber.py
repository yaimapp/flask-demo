# coding: utf-8
# functions to show chuuguu
# first written 19 Dec 2008/last updated 24 Dec 2008

# history
# 24 Dec 2008: function for the day added
# 23 Dec 2008: function for the day started to be written
# 21 Dec 2008: ported into python
# 19 Dec 2008: first draft in gawk

import nobenengappi, etonumber

# to find the number of chuuguu of the year
def getnenchuuguunumber(nobenen):
	return 9 - (nobenen - 2) % 9;

# to find the number of chuuguu of the month
def gettsukichuuguunumber(nobetsuki):
	return 9 - (nobetsuki - 1) % 9;

# to find the number of chuuguu of the day
def gethichuuguunumber(year, month, day):
	nobehi = nobenengappi.getnobehi(year, month, day);
	
	# to find last touji and geshi of the day thirty days later than given day
	# not to miss touji or geshi just after the given day
	if month == 12:
		recenttoujinobehi = getlasttoujinobehi(year + 1, 1, day);
		recentgeshinobehi = getlastgeshinobehi(year + 1, 1, day);
	else:
		recenttoujinobehi = getlasttoujinobehi(year, month + 1, day);
		recentgeshinobehi = getlastgeshinobehi(year, month + 1, day);

	youtonkirikaenobehi = getkirikaenobehi(recenttoujinobehi);
	intonkirikaenobehi = getkirikaenobehi(recentgeshinobehi);

	# test print
	#print 'nobehi, recenttoujinobehi, recentgeshinobehi, youtonkirikaenobehi, intonkirikaenobehi';
	#print nobehi, recenttoujinobehi, recentgeshinobehi, youtonkirikaenobehi, intonkirikaenobehi;

	if intonkirikaenobehi > youtonkirikaenobehi:
		if intonkirikaenobehi <= nobehi:
			return 9 - ((etonumber.gethietonumber(intonkirikaenobehi) - 1) % 27 + nobehi - intonkirikaenobehi) % 9;
		else:
			return ((etonumber.gethietonumber(youtonkirikaenobehi) - 1) % 24 + nobehi - youtonkirikaenobehi) % 9 + 1;

	else:
		if youtonkirikaenobehi <= nobehi:
			return ((etonumber.gethietonumber(youtonkirikaenobehi) - 1) % 24 + nobehi - youtonkirikaenobehi) % 9 + 1;
		else:
			return 9 - ((etonumber.gethietonumber(intonkirikaenobehi) - 1) % 27 + nobehi - intonkirikaenobehi) % 9;

# to determine the day of touji and geshi
# the days of touji and geshi are made sure to be correct between 1950 and 2050
# references
# 角田桂一、「二十四節気の略算式」、accessed 23 Dec 2008
# URL http://www.h3.dion.ne.jp/~sakatsu/sekki24_topic.htm
# 石山勝則、「天文メモ: 暦と時計: 二十四節気」、accessed 23 Dec 2008
# URL http://www.tky.3web.ne.jp/~ishiyama/waah/memo.htm#calender

def gettoujiday(year):
	return int(22.6587 + 0.242752 * (year - 1900) - int((year - 1900) / 4));

def getgeshiday(year):
	return int(22.2718 + 0.241669 * (year - 1900) - int((year - 1900) / 4));

# to find last touji of the given date
def getlasttoujinobehi(year, month, day):
	if month == 12 and day >= gettoujiday(year):
		return nobenengappi.getnobehi(year, 12, gettoujiday(year));
	else:
		return nobenengappi.getnobehi(year - 1, 12, gettoujiday(year - 1));

# to find last geshi of the given date
def getlastgeshinobehi(year, month, day):
	if month > 6 or (month == 6 and day >= getgeshiday(year)):
		return nobenengappi.getnobehi(year, 6, getgeshiday(year));
	else:
		return nobenengappi.getnobehi(year - 1, 6, getgeshiday(year - 1));

# to find kirikaenobehi or beginning date of youton or inton in nobehi
def getkirikaenobehi(nobehi):
	hietonumber = etonumber.gethietonumber(nobehi);
	if hietonumber == 1:
		return nobehi;
	if hietonumber >= 2 and hietonumber <= 29:
		return nobehi - (hietonumber - 1);
	if hietonumber == 30:
		return nobehi + 1;
	if hietonumber == 31:
		return nobehi;
	if hietonumber == 32:
		return nobehi - 1;
	if hietonumber >= 33 and hietonumber <= 60:
		return nobehi + (61 - hietonumber);

