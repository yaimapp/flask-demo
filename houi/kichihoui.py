# coding: utf-8
# function to show luck for each direction by chuuguu, eto and honmeiseinumber given
# first written 18 Dec 2008/last updated 07 Dec 2015

# history
# 07 Dec 2015: taisai added onto nenban
# 06 Dec 2015: options south (table with the south on the top), tendou of the month and teiitaichuu added
# 24 Dec 2008: table formatting added
# 21 Dec 2008: ported into python
# 19 Dec 2008: annotations added; function name changed
# 18 Dec 2008: first draft in gawk

def getkichihoui(chuuguunumber, etonumber, honmeiseinumber, format, topdirection, tendou, taisai, taichuu):

# numbers to be applied for each parameter:
# chuuguunumber: 1 to 9 ("first white water star" to "ninth purple fire star")
# etonumber: 1 to 60 ("first" mouse to "tenth" boar)
# honmeiseinumber: 1 to 9 ("first white water star" to "ninth purple fire star")
# format: "list or table"
# topdirection: "north or south"
# tendou: "-1 to 12"
# taisai: "yes or no"
# taichuu: "yes or no"

	# to set default for chuuguunumber 5 or "fifth yellow earth star"
	if chuuguunumber == 0 or chuuguunumber == '':
		chuuguunumber = 5;

	# to arrange directions in order (clockwise)
	directionbynumber = {0: 'center', 1: 'north', 2: 'northeast', 3: 'east', 4: 'southeast', 5: 'south', 6: 'southwest', 7: 'west', 8: 'northwest'};

	# to correspond each direction with that in Chinese characters
	directioninchinesecharacter = {'center': '中宮', 'northwest': '西北', 'west': '西', 'northeast': '東北', 'south': '南', 'north': '北', 'southwest': '西南', 'east': '東', 'southeast': '東南'};

	# to correspond each direction with each number of the stars
	kyuusei = {'center': chuuguunumber % 9, 'northwest': (chuuguunumber + 1) % 9, 'west': (chuuguunumber + 2) % 9, 'northeast': (chuuguunumber + 3) % 9, 'south': (chuuguunumber + 4) % 9, 'north': (chuuguunumber + 5) % 9, 'southwest': (chuuguunumber + 6) % 9, 'east': (chuuguunumber + 7) % 9, 'southeast': (chuuguunumber + 8) % 9};
	for direction in kyuusei:
		if kyuusei[direction] == 0:
			kyuusei[direction] += 9;

	# to initialise variables of luck for each direction
	kikkyou = {'center': '', 'northwest': '', 'west': '', 'northeast': '', 'south': '', 'north': '', 'southwest': '', 'east': '', 'southeast': ''};

	# to identify goousatsu and honmeisatsu
	for direction in kyuusei:
		if kyuusei[direction] == 5 or kyuusei[direction] == honmeiseinumber:
			kikkyou[direction] = kikkyou[direction] + '×';

	# to identify ankensatsu and honmeitekisatsu
	if kyuusei['north'] == 5 or kyuusei['north'] == honmeiseinumber:
		kikkyou['south'] = kikkyou['south'] + '×';
	if kyuusei['northeast'] == 5 or kyuusei['northeast'] == honmeiseinumber:
		kikkyou['southwest'] = kikkyou['southwest'] + '×';
	if kyuusei['east'] == 5 or kyuusei['east'] == honmeiseinumber:
		kikkyou['west'] = kikkyou['west'] + '×';
	if kyuusei['southeast'] == 5 or kyuusei['southeast'] == honmeiseinumber:
		kikkyou['northwest'] = kikkyou['northwest'] + '×';
	if kyuusei['south'] == 5 or kyuusei['south'] == honmeiseinumber:
		kikkyou['north'] = kikkyou['north'] + '×';
	if kyuusei['southwest'] == 5 or kyuusei['southwest'] == honmeiseinumber:
		kikkyou['northeast'] = kikkyou['northeast'] + '×';
	if kyuusei['west'] == 5 or kyuusei['west'] == honmeiseinumber:
		kikkyou['east'] = kikkyou['east'] + '×';
	if kyuusei['northwest'] == 5 or kyuusei['northwest'] == honmeiseinumber:
		kikkyou['southeast'] = kikkyou['southeast'] + '×';

	# to identify ha
	juunishinumber = (etonumber - 1) % 12 + 1;
	if juunishinumber == 1:
		kikkyou['south'] = kikkyou['south'] + '×';
	if juunishinumber == 2 or juunishinumber == 3:
		kikkyou['southwest'] = kikkyou['southwest'] + '×';
	if juunishinumber == 4:
		kikkyou['west'] = kikkyou['west'] + '×';
	if juunishinumber == 5 or juunishinumber == 6:
		kikkyou['northwest'] = kikkyou['northwest'] + '×';
	if juunishinumber == 7:
		kikkyou['north'] = kikkyou['north'] + '×';
	if juunishinumber == 8 or juunishinumber == 9:
		kikkyou['northeast'] = kikkyou['northeast'] + '×';
	if juunishinumber == 10:
		kikkyou['east'] = kikkyou['east'] + '×';
	if juunishinumber == 11 or juunishinumber == 12:
		kikkyou['southeast'] = kikkyou['southeast'] + '×';

	# to identify teiitaichuu
	if taichuu == "yes":
		if kyuusei['north'] == 9:
			kikkyou['north'] = kikkyou['north'] + '×';
		if kyuusei['south'] == 1:
			kikkyou['south'] = kikkyou['south'] + '×';
	
	# to identify soukoku
	for direction in kyuusei:
		if honmeiseinumber == 1 and (kyuusei[direction] == 2 or kyuusei[direction] == 5 or kyuusei[direction] == 8 or kyuusei[direction] == 9) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
		if honmeiseinumber == 2 and (kyuusei[direction] == 1 or kyuusei[direction] == 3 or kyuusei[direction] == 4) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
		if honmeiseinumber == 3 and (kyuusei[direction] == 2 or kyuusei[direction] == 5 or kyuusei[direction] == 6 or kyuusei[direction] == 7 or kyuusei[direction] == 8) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
		if honmeiseinumber == 4 and (kyuusei[direction] == 2 or kyuusei[direction] == 5 or kyuusei[direction] == 6 or kyuusei[direction] == 7 or kyuusei[direction] == 8) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
		if honmeiseinumber == 5 and (kyuusei[direction] == 1 or kyuusei[direction] == 3 or kyuusei[direction] == 4) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
		if honmeiseinumber == 6 and (kyuusei[direction] == 3 or kyuusei[direction] == 4 or kyuusei[direction] == 9) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
		if honmeiseinumber == 7 and (kyuusei[direction] == 3 or kyuusei[direction] == 4 or kyuusei[direction] == 9) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
		if honmeiseinumber == 8 and (kyuusei[direction] == 1 or kyuusei[direction] == 3 or kyuusei[direction] == 4) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
		if honmeiseinumber == 9 and (kyuusei[direction] == 1 or kyuusei[direction] == 6 or kyuusei[direction] == 7) and kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '△';
	# to identify lucky directions
	for direction in kyuusei:
		if kikkyou[direction] == '':
			kikkyou[direction] = kikkyou[direction] + '○';

	# to show tendou
	if tendou == 1 or tendou ==5:
		kikkyou['west'] = kikkyou['west'] + '天道';
	if tendou == 2 or tendou ==10:
		kikkyou['south'] = kikkyou['south'] + '天道';
	if tendou == 3:
		kikkyou['southwest'] = kikkyou['southwest'] + '天道';
	if tendou == 4 or tendou ==8:
		kikkyou['north'] = kikkyou['north'] + '天道';
	if tendou == 6:
		kikkyou['northwest'] = kikkyou['northwest'] + '天道';
	if tendou == 7 or tendou ==11:
		kikkyou['east'] = kikkyou['east'] + '天道';
	if tendou == 9:
		kikkyou['northeast'] = kikkyou['northeast'] + '天道';
	if tendou == 12:
		kikkyou['southeast'] = kikkyou['southeast'] + '天道';

	# to show taisai
	if taisai == "yes":
		if juunishinumber == 1:
			kikkyou['north'] = kikkyou['north'] + '大歳';
		if juunishinumber == 2 or juunishinumber == 3:
			kikkyou['northeast'] = kikkyou['northeast'] + '大歳';
		if juunishinumber == 4:
			kikkyou['east'] = kikkyou['east'] + '大歳';
		if juunishinumber == 5 or juunishinumber == 6:
			kikkyou['southeast'] = kikkyou['southeast'] + '大歳';
		if juunishinumber == 7:
			kikkyou['south'] = kikkyou['south'] + '大歳';
		if juunishinumber == 8 or juunishinumber == 9:
			kikkyou['southwest'] = kikkyou['southwest'] + '大歳';
		if juunishinumber == 10:
			kikkyou['west'] = kikkyou['west'] + '大歳';
		if juunishinumber == 11 or juunishinumber == 12:
			kikkyou['northwest'] = kikkyou['northwest'] + '大歳';

	# to identify chuuguu
	kikkyou['center'] = '−';

	# to print fortunes for each direction
	if format == 'list' or format == 'l':
		print('方位\t', end=' ');

		for i in range(9):
			print('\t' + directioninchinesecharacter[directionbynumber[i]], end=' ');
		print('');
		print('九星\t', end=' ');
		for i in range(9):
			print('\t', kyuusei[directionbynumber[i]], end=' ');
		print('');
		print('吉凶\t', end=' ');
		for i in range(9):
			print('\t' + kikkyou[directionbynumber[i]], end=' ');
		print('');

	else:
		a = [8, 1, 2];
		if topdirection == 'south':
			a= [4, 5, 6];
		print('方位\t', end=' ');
		for i in a:
			print('\t' + directioninchinesecharacter[directionbynumber[i]], end=' ');
		print('');
		print('九星\t', end=' ');
		for i in a:
			print('\t', kyuusei[directionbynumber[i]], end=' ');
		print('');
		print('吉凶\t', end=' ');
		for i in a:
			print('\t' + kikkyou[directionbynumber[i]], end=' ');
		print('');

		a = [7, 0, 3];
		if topdirection == 'south':
			a= [3, 0, 7];
		print('方位\t', end=' ');
		for i in a:
			print('\t' + directioninchinesecharacter[directionbynumber[i]], end=' ');
		print('');
		print('九星\t', end=' ');
		for i in a:
			print('\t', kyuusei[directionbynumber[i]], end=' ');
		print('');
		print('吉凶\t', end=' ');
		for i in a:
			print('\t' + kikkyou[directionbynumber[i]], end=' ');
		print('');

		a = [6, 5, 4];
		if topdirection == 'south':
			a= [2, 1, 8];
		print('方位\t', end=' ');
		for i in a:
			print('\t' + directioninchinesecharacter[directionbynumber[i]], end=' ');
		print('');
		print('九星\t', end=' ');
		for i in a:
			print('\t', kyuusei[directionbynumber[i]], end=' ');
		print('');
		print('吉凶\t', end=' ');
		for i in a:
			print('\t' + kikkyou[directionbynumber[i]], end=' ');
		print('');
