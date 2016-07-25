#!/usr/bin/env python3

"""
Script from Automate the Boring Stuff to place some address on the CLIPBOARD then run this from the COMMANLINE and your default browser goes to the address on Google Maps.

The Google starting place is: https://www.google.com/maps/place/<address here>

The address substituted into <address here> does not have to be complete! Try a full home address for someone.... just copy nada tom the clipboard and run it and see where nada is!

At CLI just do this;

rdw99$ python3 /Users/rdw99/Python/mapit.py

Takes you to Nada Ohio.

sys.argv holds commandline arguments
sys.argv will be a [LIST] with mapit.py at index 0
So to check if there is an address in the list after index 0 we do an if length on it to see if it is > 1.
Also the address will be multiple short strings for st #, st name, st or road  or lane etc.
These need to be put into 1 str with the join method
"""


import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:
	address=' '.join(sys.argv[1:])
else:
	address=pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)