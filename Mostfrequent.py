
#most frequent characters 
import operator
str = input("please enter a string : ") 
 
count={}
for x in str:
    if x in count.keys():
      count[x] = count[x]+ 1
    else:
      count[x]=1
dst=dict(sorted(count.items(),key=operator.itemgetter(1),reverse=True))
for x in dst:
    print(x," = ",count[x])
