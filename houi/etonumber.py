# function to show number of eto
# first written 19 Dec 2008/last updated 23 Dec 2008

# history
# 23 Dec 2008: eto extended to sixty elements
#              function for the day added
# 21 Dec 2008: ported into python
# 19 Dec 2008: first draft in gawk

def getnen_etonumber(nobenen):
	return (nobenen - 4) % 60 + 1;

def gettsukietonumber(nobetsuki):
	return (nobetsuki + 24) % 60 + 1;

def gethietonumber(nobehi):
	return (nobehi + 14) % 60 + 1;

