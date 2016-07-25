"""
SENTDEX Python Basics Tutorial Video 36 on REGEX
Regular Expressions

IDENTIFIERS 
\d=decimal
\D=NAN, \s=space
\S=Anything but a SPACE
\w=any CHAR
\W anything but a CHAR
.=Any CHAR EXCEPT NEWLINE
\b=WhiteSpace around words
\. A period

MODIFIERS for Numbers:
{1,3} we're expecting 1-3 digits
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of a string
^ Matching the beginning of a string
| Either OR
[] Range or "Variance" eg. [1-5a-qA-Z]
{x} expecting "x" amount

WHITE SPACE CHARACTERS
\n for NEWLINE
\s SPACE
\t TAB
\e ESCAPE
\f FORM FEED
\r RETURN

DON'T FORGET!!!!! If you want to REALLY use the follwing CHAR you must ESCAPE them
So to use a \ for real you must do it twice--> \\
So to use a . for real you must--> \.
etc.

. + * ? [ ] $ ^ ( ) { } | \

RE.FINADALL is very common and a lot of users may only use that. He will cover more on this later.

CODE from Automate the Boring Stuff regex Video showing a FUNCTION with other COMMANDS like RE.COMPILE and PATTERN.MATCH Method.

from re import *
pattern=compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)[a-z]{2,6}(\s|$)')

def get_address():
	address=input('Enter Your Email Address:')
	is_valid=pattern.match(address)
	
	if is_valid:
		print('Valid Address:', is_valid.group())
	else:
		print('Invalid Address! Please Retry...\n')		
get_address()
"""
import re

exampleString='''
Jessica is 15 years old, and Daniel is 27 years old.
Srangavissayarangakakitpornsabuvasdanobbaklu is 97, and his grandfather, Bob is 102.
'''

ages=re.findall(r'\d{1,3}',exampleString) #find 1-3 decimals together and grab em
#NAMES find any # of CAPs 1st letter only then 0 or MORE lowercase CHAR so any #
#This all stops at end of a word then looks for next name in the pattern
#The * is the 0 or more MODIFIE so makes [a-z] mean any amount lowercase letters
names=re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

#Make a dictionary of the 2 Items
ageDict={}
x=0
for eachName in names:
	ageDict[eachName]=ages[x]
	x+=1

print(ageDict)













