"""
Advanced String Formatting from 2nd 1/2 of this page;
---> http://www.python-course.eu/python3_formatted_output.php

String Format SYNTAX with Format Code and using DOT.FORMAT Method

---> "blahblah {formatcode1} blah blah {formatcode2}".format (1,2)

Here a long string has 2 formatted items {} to be substituted in from the 2 ARG in () after.
The code in {} is not printed so if you really want {} inside you muse ESCAPE them like this {{}}.

INDEXING Inside {} is with a : instead of % and is 0-end so eg {0:code} blah {1:code) for 2 arg
{0} {1} {2 is optional if arg kept in order but if you want to rearrange them you must show the index eg {} {} {} is for arg1 arg2 arg3 -no need to put index number but for {2} {3} {1} not optional.

DOT.FORMAT has Indexed POSITIONAL p args (arg1=p1, arg2=p2 etc). Also may have 0 or > KEYWORD ARGS in (name=value) form.
so (p1,p2,p3,k1(name=value),k2(name=value),k3(name=value))

example {index1:5d} for 5 decimal places {index2:8.2f} for a float total 8 places and rounded to 2 digits after period (just like for PRINT FORMATTING same URL)

Now the format below should be easy to read::: replace {0} with 47 and {1} with 11
"First argument: {0}, second one: {1}".format(47,11)
"First argument: {}, second one: {}".format(47,11) #is the same.

But could have been to switch around the substitutions;
"First argument: {1}, second one: {0}".format(47,11)

"""

#Disgruntled Wall Strret employee who lost 0.00489 off his paycheck!!!!!
# Shows you can dictate PRECISION with the formatting
s1="I was paid {0:8.2f} but I wanted to be paid {0:8.5f} so I got screwed!".format (982000.54489499)
print(s1,'\n')

s2="Tesla Model: {a:5d},  Price: {p:.2f}".format (a=626, p=59000.058)
print(s2,end='\n')
print(s2,'\n') #Same as prior

"""
OPTIONS for JUSTIFY(<^>) SEPARATE(,) SIGN(+ or -) and PRENUMBER PADDING(0 or =) FORMATTING
#Use FORMAT to dictate SPACES only for arg1 why not arg 2??????
#the s in {} is optional it seems. The s in s=STR is short for String
"""
s3="{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99) #Python does least amount of work
s4="{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99) #arg2 seems fixed I don't know why
s5="{0:<20} {1:6.2f}".format('Spam & Ham:', 7.99) #NO s after <20 so s not required
print(s3)
print(s4)
print(s5)
"""
OPTIONS== 
< -Justify L
> -Justify R
o -Leading 0 PADDING( 00000137)
, -Thousands Separator{:,}-->(76,483,609) or {0:6,d}-->
= -SIGN-Leading-0 PADDING(+00000137)
^ -Forced CENTERing
SIGN OPTIONS==
+ -Place Proper SIGN before any digit + or -. Neg to + and places a sign at both
- -Place a - SIGN before NEG numbers only. Just used for NEG numbers
space -Leading SPACE before + numbers and a place for the - SIGN
"""

x=5897653423
print("The value is {:,}".format(x)) #put in some COMMAs
print("The value is {0:6,d}".format(x)) #

x=5897653423.89676
print("The value is {0:12,.3f}".format(x)) #COMMAs and FLOATs Here!!

print("The capital of {0:s} is {1:s}".format("Ontario","Toronto")) #space OPTION here
print("The capital of {0:} is {1:}".format("Ontario","Toronto")) #without the space OPTION is same!

#Now with **keyword ARG
print("The capital of {0:s} is {1:s}".format("Ontario","Toronto"))
print("The capital of {province} is {capital}".format(province="Ontario",capital="Toronto"))

#**kwargs for DICT substitution work also but they went for hours on this example.
#print("The capital of {province} is {capital}".format(**k))
#Also other STR methods like ljust, rjust, center etc.

