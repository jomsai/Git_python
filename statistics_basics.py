import math, statistics
from fractions import Fraction as F

data1=[92,88,82,69,76,84,98,70,82,82,90,96,90,84,76,82,90]
mu1=statistics.mean(data1)
data2=[166,154,134,128,166,168,155,177,166,143,125]
mu2=statistics.mean(data2)
print(mu1)
print(mu2)
#print(statistics.mean(data1))
#Need a median and interpolated value is ok
print(statistics.median(data1))

#Need a median that is actually in the set of data1
#82 was median but not in data1
print(statistics.median_low(data1))
print(statistics.mode(data1))
print(statistics.stdev(data1))
#Variance is a measure of variation of the data
#Variance with 2nd arg so that it recalculates the mean
#This 2nd is optional but mean as mu1 was already calulated
#Avoids recalc of mean -just inserts prior value
print('Variance of mu1 is: ',statistics.variance(data1,mu1))

#Most common item is the mode
print(statistics.mode(data2))
print(statistics.mean(data2))
print(statistics.stdev(data2))
print(statistics.median(data2))
print(statistics.median_grouped(data2))

print('Variance data2 is: ',statistics.pvariance(data2))

# OK now take the mean of 4 fractions
# This works in iPython Notebook
print(statistics.mean([F(1,2),F(1,2),F(1,3),F(1,4)]))
print(statistics.mean([F(876,1437),F(7296,43781),F(1208,1655),F(988,1659)]))
print(statistics.mean([F(6,4),F(12,8),F(69,14),F(721,562)]))
