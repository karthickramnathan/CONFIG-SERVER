from datetime import date
from re import A
import pandas as y
import numpy as x
y.read_csv("book1 female.csv")
y.read_csv("book1 male.csv")
print("enter the sex")

sex=input()
if sex=="male":
   male= y.read_csv("book1 male.csv",parse_dates=True,dayfirst=True,index_col=0)
   j=male.groupby(y.Grouper(freq="M")).mean()
   q=y.DataFrame(j)
   r=q.iloc[0:5,2]
   print("maximum ctscore",max(r))
   print("maximum ctscore",min(r))
   s=q.iloc[0:5,3]
   print("maximum spo2",max(s))
   print("minimum spo2",min(s))
   b=int(input("enter the ct score"))
   c=int(input("enter spo2 level"))
   if b > max(r) or c > max(s):
      print("very severe")
      print("take to the hospital\n hurry up")
   elif (b<max(r) and b> min(r)) or (c < max(s) and c >min(s)):
      print("moderate severity")
   elif b < min(r) or c < min(s):
      print("not severe")
   else:
      print("wrong input")   
elif sex=="female":
   female= y.read_csv("book1 female.csv",parse_dates=True,dayfirst=True,index_col=0)
   k=female.groupby(y.Grouper(freq="M")).mean()
   print(k)
   w=y.DataFrame(k)
   e=w.iloc[0:5,2]
   print("maximum ctscore",max(e))
   print("maximum ctscore",min(e))
   f=w.iloc[0:5,3]
   print("maximum spo2",max(f))
   print("minimum spo2",min(f))
   b=int(input("enter the ct score"))
   c=int(input("enter spo2 level"))
   if b > max(e) or c > max(f):
      print("very severe")
   elif (b<max(e) and b> min(e)) or (c < max(f) and c >min(f)):
      print("moderate sevirity")
   elif b < min(e) or c < min(f):
      print("no problem")
   else:
      print("wrong input")   


