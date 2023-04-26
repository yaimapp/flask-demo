# coding: utf-8
# functions to find setsuiribi or setsuri-days
# first written 24 Dec 2008/last updated 03 Jan 2009

# history
# 07 Apr 2011: URL updated
# 24 Dec 2008: first draft

# references
# 角田桂一、「二十四節気の略算式」、accessed 23 Dec 2008
# URL http://www.h3.dion.ne.jp/~sakatsu/sekki24_topic.htm
# 石山勝則、「天文メモ: 暦と時計: 二十四節気」、accessed 07 Apr 2011
# URL http://i.gmobb.jp/ishiyama/waah/memo.htm#calender

def getsetsuiriday(year, month):
	if month == 1:
		return int(6.3857 + 0.242778 * (year - 1900) - int((year - 1900) / 4));
	if month == 2:
		return int(4.8693 + 0.242713 * (year - 1900) - int((year - 1900) / 4));
	if month == 3:
		return int(6.3968 + 0.242512 * (year - 1900) - int((year - 1900) / 4));
	if month == 4:
		return int(5.6303 + 0.242231 * (year - 1900) - int((year - 1900) / 4));
	if month == 5:
		return int(6.3771 + 0.241945 * (year - 1900) - int((year - 1900) / 4));
	if month == 6:
		return int(6.5733 + 0.241731 * (year - 1900) - int((year - 1900) / 4));
	if month == 7:
		return int(8.0091 + 0.241642 * (year - 1900) - int((year - 1900) / 4));
	if month == 8:
		return int(8.4102 + 0.241703 * (year - 1900) - int((year - 1900) / 4));
	if month == 9:
		return int(8.5252 + 0.241898 * (year - 1900) - int((year - 1900) / 4));
	if month == 10:
		return int(9.1475 + 0.242179 * (year - 1900) - int((year - 1900) / 4));
	if month == 11:
		return int(8.2419 + 0.242469 * (year - 1900) - int((year - 1900) / 4));
	if month == 12:
		return int(7.9138 + 0.242689 * (year - 1900) - int((year - 1900) / 4));

def getsetsuirinichiji(year, month):
	if month == 1:
		return 6.3857 + 0.242778 * (year - 1900) - int((year - 1900) / 4);
	if month == 2:
		return 4.8693 + 0.242713 * (year - 1900) - int((year - 1900) / 4);
	if month == 3:
		return 6.3968 + 0.242512 * (year - 1900) - int((year - 1900) / 4);
	if month == 4:
		return 5.6303 + 0.242231 * (year - 1900) - int((year - 1900) / 4);
	if month == 5:
		return 6.3771 + 0.241945 * (year - 1900) - int((year - 1900) / 4);
	if month == 6:
		return 6.5733 + 0.241731 * (year - 1900) - int((year - 1900) / 4);
	if month == 7:
		return 8.0091 + 0.241642 * (year - 1900) - int((year - 1900) / 4);
	if month == 8:
		return 8.4102 + 0.241703 * (year - 1900) - int((year - 1900) / 4);
	if month == 9:
		return 8.5252 + 0.241898 * (year - 1900) - int((year - 1900) / 4);
	if month == 10:
		return 9.1475 + 0.242179 * (year - 1900) - int((year - 1900) / 4);
	if month == 11:
		return 8.2419 + 0.242469 * (year - 1900) - int((year - 1900) / 4);
	if month == 12:
		return 7.9138 + 0.242689 * (year - 1900) - int((year - 1900) / 4);
