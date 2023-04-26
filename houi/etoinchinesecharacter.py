# coding: utf-8
# function to show the "extended" animal of the year
# first written 19 Dec 2008/last updated 23 Dec 2008

# history
# 23 Dec 2008: eto extended to sixty elements
# 21 Dec 2008: ported into python
# 19 Dec 2008: first draft in gawk

def getetoinchinesecharacter(etonumber):

	jikkannumber = (etonumber - 1) % 10 + 1;
	juunishinumber = (etonumber - 1) % 12 + 1;

	if jikkannumber == 1:
		jikkan = '甲';
	if jikkannumber == 2:
		jikkan = '乙';
	if jikkannumber == 3:
		jikkan = '丙';
	if jikkannumber == 4:
		jikkan = '丁';
	if jikkannumber == 5:
		jikkan = '戊';
	if jikkannumber == 6:
		jikkan = '己';
	if jikkannumber == 7:
		jikkan = '庚';
	if jikkannumber == 8:
		jikkan = '辛';
	if jikkannumber == 9:
		jikkan = '壬';
	if jikkannumber == 10:
		jikkan = '癸';

	if juunishinumber == 1:
		juunishi = '子';
	if juunishinumber == 2:
		juunishi = '丑';
	if juunishinumber == 3:
		juunishi = '寅';
	if juunishinumber == 4:
		juunishi = '卯';
	if juunishinumber == 5:
		juunishi = '辰';
	if juunishinumber == 6:
		juunishi = '巳';
	if juunishinumber == 7:
		juunishi = '午';
	if juunishinumber == 8:
		juunishi = '未';
	if juunishinumber == 9:
		juunishi = '申';
	if juunishinumber == 10:
		juunishi = '酉';
	if juunishinumber == 11:
		juunishi = '戌';
	if juunishinumber == 12:
		juunishi = '亥';

	return jikkan + juunishi;
