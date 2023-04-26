# coding: utf-8
# function to show honmeisei
# first written 21 Dec 2008/last updated 05 Dec 2015

# history
# 05 Dec 2015: added the case '無し(None)'
# 21 Dec 2008: first draft in python

def gethonmeisei(honmeiseinumber):
	if honmeiseinumber == 1:
		return '一白水星';
	if honmeiseinumber == 2:
		return '二黒土星';
	if honmeiseinumber == 3:
		return '三碧木星';
	if honmeiseinumber == 4:
		return '四緑木星';
	if honmeiseinumber == 5:
		return '五黄土星';
	if honmeiseinumber == 6:
		return '六白金星';
	if honmeiseinumber == 7:
		return '七赤金星';
	if honmeiseinumber == 8:
		return '八白土星';
	if honmeiseinumber == 9:
		return '九紫火星';
	return '無し';
