import statistics
from fractions import Fraction as F

x=[7,8,5,9,7,6,8,6,7,7,9,8,8,8,5]
mu=statistics.mean(x)
print(mu)

med=statistics.median(x)
print(med)

mod=statistics.mode(x)
print(mod)

var=statistics.variance(x)
print(var)

med_lo=statistics.median_low(x)
print(med_lo)

sdev=statistics.stdev(x)
print(sdev)

med_grp=statistics.median_grouped(x)
print(med_grp)

#Fractions are easy also
frac=[F(1,2),F(1,2),F(1,3),F(1,4)]
mu_frac=statistics.mean(frac)
print(mu_frac)