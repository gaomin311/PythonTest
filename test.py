#!/usr/bin/python

def GetRank(a):
	for eachNum in a:
		if 90 <= eachNum <= 100:
			print 'A'
		elif 80 <= eachNum <= 89:
			print 'B'
		elif 70 <= eachNum <= 79:
			print 'C'
		elif 60 <= eachNum <= 69:
			print 'D'
		elif eachNum < 60:
			print 'F'
		else:
			print '';

#is a leap year
def IsLeapYear(a): 
	b = a % 4;
	c = a % 100;
	d = a % 400;
	if (0 == b and 0 != c) or (0 == d):
		return True
	else:
		return False

#test code
for eachNum in (1992, 1996, 2000, 1967, 1900, 2400):
	print IsLeapYear(eachNum)

