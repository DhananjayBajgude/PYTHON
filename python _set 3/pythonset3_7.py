import math
data=[12,212,121,12,12,12,111,43]
sum=0
for i in data:
    print(i)
mean=sum/(data) 
var=0
for i in data:
    var=var+math.pow((mean-1),2)
var=var/data
sd=math.sqrt(var)
mean=mean-sd
mean=mean+sd
print("the range % to be is obtain ",mean,"to",mean)    
    
