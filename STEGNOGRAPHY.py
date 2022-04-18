from dataclasses import replace
from pickle import TRUE
import string
from cv2 import imshow
import numpy as x
import pandas as y
import matplotlib.image as i
import matplotlib.pyplot as p
z=i.imread("pic1.jpg")
x.array(z)
print("original shape",z.shape)
s=z.flatten()
print(s)
message=input("enter the message:")
a=list(message)
print("**********ENCODING***************")
for i in range (0,len(a)):  
     s[i]=ord(a[i] ) 
print(s)
d=s.reshape(z.shape) 
p.imshow(d)
print("encoded message shape",d.shape) 
print("***********DECODING***************")
print("**********************comparing original and duplicate  image****************")
q=x.equal(z,d)
c=d[q==False]
f=[]
for i in range (0,len(c)):
    g = (chr(c[i]))
    f.append(g)
new=""
for k in range (0,len(f)):
     new+=f[k]
print( "decoded message:",new)


    



    

    
    
 




