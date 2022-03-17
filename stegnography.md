# stegnography
import numpy as x
import pandas as y
import matplotlib.image as i
import matplotlib.pyplot as p
z=i.imread("pic1.jpg")
c=x.array(z)
d=z.reshape(z.shape[0],-1)
#print(d)
y.DataFrame(d)
m=input("enter the message:")
a=list(m)
print("**********ENCODING***************")
for i in range (0,len(a)):  
     d[0,i]=ord(a[i] ) 
#print(d)    
s=d.reshape(z.shape)
#print(s)
print("***********DECODING***************")
print("**********************comparing original and duplicate  image****************")
q=x.equal(c,s)
#print(q)
c=s[q==False]
f=[]
for i in range (0,len(c)):
    g = (chr(c[i]))
    f.append(g)
new=""
for k in range (0,len(f)):
     new+=f[k]
print( "DECODED MESSAGE:",new)
