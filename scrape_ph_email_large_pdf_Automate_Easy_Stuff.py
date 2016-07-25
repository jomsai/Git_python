#!/usr/bin/python
"""
From Automate the Boring Stuff with Python Chapter 7
Extract phone numbers and emails from a huge PDF file

NOTE: re.VERBOSE method allows us to put a huge command in triple quotes AND do #comments inside it!

WEAKNESS: Lists all Phones then all emails. Better if they matched. ALSO many of the numbers are FAXES

Final Results placed on CLIPBOARD so need to paste data in an email or text file.
"""

import re, pyperclip

phoneRegex=re.compile(r'''
#xxx-xxx-xxxx or xxx-xxxx or (xxx) xxx-xxxx ext. xxxx 
# or #xxx.xxx.xxxx etc formats needed.
#GROUPS important so parentheses over all below PH format
# and each subgroup. ???? = OPTIONAL

(
((\d\d\d)) | (\(\d\d\d))?
(\s | -)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s) |x)
(\d{2,5}))?
)

''', re.VERBOSE

emailRegex=re.compile(r'''

#user_or.or-or+@domainDOTcomORnet etc
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+)

''', re.VERBOSE)

text=pyperclip.paste()

extractedPhone=phoneRegex.findall(text)
extractedEmail=emailRegex.findall(text)

allPhoneNumbers=[]
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedEmail)

results='\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)




