#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# function to show luck for directions of the month and the year
# first written 18 Dec 2008/last updated 07 Dec 2015

# history
# 07 Dec 2015: taisai added onto nenban
# 06 Dec 2015: options south (table with the south on the top), tendou of the month and teiitaichuu (north/south) added
# 04 Dec 2015: argparse, the recommended command-line parsing module employed
# 23 Nov 2015: ported into python3 (ver. 3.4.2)
# 01 Mar 2012: bug fixed at nobenengappi.py
# 30 Oct 2011: bug fixed
# 09 Oct 2009: bug fixed
# 30 Apr 2009: time display updated to avoid "60 minutes" eg 11:60
# 03 Jan 2009: time of setsuiri added
# 27 Dec 2008: list of the year, month or day to be printed according to the length of date
# 24 Dec 2008: setsuiribi or setsuiri-days added
#              names of functions and variables made tidy
# 23 Dec 2008: eto extended to sixty elements
#              hiban added
#              some functions merged into files to keep them tidy
# 21 Dec 2008: ported into python
# 18 Dec 2008: first draft in gawk

import sys, string, datetime, argparse
from honmeisei import *
from etoinchinesecharacter import *
from nobenengappi import *
from chuuguunumber import *
from etonumber import *
from setsuiriday import *
from kichihoui import *

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="honmeisei number: 1 to 9")
parser.add_argument("y", type=int, help="date in digits: year (1950 to 2050) [+ month [+ day]], eg 2015, 201501, 20150102")
parser.add_argument("-l", "--list", action="store_true", help="print list instead of table")
parser.add_argument("-s", "--south", action="store_true", help="print table with the south on the top (default: north on top)")
parser.add_argument("-T", "--tendou", action="store_true", help="print tendou of the month")
parser.add_argument("-t", "--taichuu", action="store_true", help="include teiitaichuu (north/south)")
args = parser.parse_args()

format = "table";
if args.list:
	format = "list";

topdirection = "north";
if args.south:
	topdirection = "south";

tendou = -1;
if args.tendou:
	tendou = 0;

taichuu = "no";
if args.taichuu:
	taichuu = "yes";

taisai = "no";

honmeiseinumber = args.x;
if honmeiseinumber < 1 or honmeiseinumber > 9:
	honmeiseinumber = 0;

date = args.y;
year = month = day = 0;
if 1950 <= date <= 2050:
	year = date;
	taisai = "yes";
elif 195001 <= date <= 205012:
	year = date // 100;
	month = date % 100;
	if month > 12:
		print("月は1〜12の範囲で指定願います。");
		print("代りに年盤を表示します。");
		month = 0;
elif 19500101 <= date <= 20501231:
	year = date // 10000;
	month = date % 10000 // 100;
	if month > 12:
		print("月は1〜12の範囲で指定願います。");
		print("代りに年盤を表示します。");
		month = 0;
	else:
		day = date % 100;
		if day > 31:
			print("日は1〜31の範囲で指定願います。");
			print("代りに月盤を表示します。");
			day = 0;
else:
	print("日にちは年(1950〜2050)、年月(195001〜205012)または年月日(19500101〜20501231)の範囲で指定願います。");
	print("代りに今日の日盤を表示します。")
	d = datetime.datetime.today();
	year = d.year;
	month = d.month;
	day = d.day;

honmeisei = gethonmeisei(honmeiseinumber);
nobenen = getnobenen(year);
nobetsuki = getnobetsuki(year, month);
nobehi = getnobehi(year, month, day);

nenchuuguunumber = getnenchuuguunumber(nobenen);
nen_etonumber = getnen_etonumber(nobenen);
tsukichuuguunumber = gettsukichuuguunumber(nobetsuki);
tsukietonumber = gettsukietonumber(nobetsuki);
hichuuguunumber = gethichuuguunumber(year, month, day);
hietonumber = gethietonumber(nobehi);

if month <= 2:
	modifiedyear = year - 1;
else:
	modifiedyear = year;

def getyearlylist(year):
	setsuiriday = getsetsuiriday(modifiedyear, 2);
	setsuirinichiji = getsetsuirinichiji(modifiedyear, 2);
	setsuirijikoku = setsuirinichiji - int(setsuirinichiji);
	setsuiriji = int(24 * setsuirijikoku);
	setsuirifun = int(60 * (24 * setsuirijikoku - int(24 * setsuirijikoku)) + 0.5);

	if setsuirifun == 60:
		setsuirifun = 0;
		setsuiriji += 1;
		if setsuiriji == 24:
			setsuiriji = 0;
			setsuiriday += 1;

	print('年盤:', str(year),  '年、節入り日:', '2', '月', str(setsuiriday), '日', str(setsuiriji), '時', str(setsuirifun), '分');
	print('年干支:', getetoinchinesecharacter(nen_etonumber));
	getkichihoui(nenchuuguunumber, nen_etonumber, honmeiseinumber, format, topdirection, tendou, taisai, taichuu);
	print();

def getmonthlylist(year, month):
	setsuiriday = getsetsuiriday(modifiedyear, month);
	setsuirinichiji = getsetsuirinichiji(modifiedyear, month);
	setsuirijikoku = setsuirinichiji - int(setsuirinichiji);
	setsuiriji = int(24 * setsuirijikoku);
	setsuirifun = int(60 * (24 * setsuirijikoku - int(24 * setsuirijikoku)) + 0.5);

	if setsuirifun == 60:
		setsuirifun = 0;
		setsuiriji += 1;
		if setsuiriji == 24:
			setsuiriji = 0;
			setsuiriday += 1;

	print('月盤:', str(year), '年', str(month), '月、節入り日:', str(month), '月', str(setsuiriday), '日', str(setsuiriji), '時', str(setsuirifun), '分');
	print('月干支:', getetoinchinesecharacter(tsukietonumber));
	getkichihoui(tsukichuuguunumber, tsukietonumber, honmeiseinumber, format, topdirection, tendou, taisai, taichuu);
	print();

def getdailylist(year, month, day):
	print('日盤:', str(year),  '年', str(month), '月', str(day), '日');
	print('日干支:', getetoinchinesecharacter(hietonumber));
	getkichihoui(hichuuguunumber, hietonumber, honmeiseinumber, format, topdirection, tendou, taisai, taichuu);
	print();

# to print out the results
print('本命星:', honmeisei);

if month == day == 0:
	getyearlylist(year);

elif day == 0:
	if tendou == 0:
		tendou = month;
	getmonthlylist(year, month);

else:
	getdailylist(year, month, day);

