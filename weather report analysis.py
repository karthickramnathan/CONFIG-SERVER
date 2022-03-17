from statistics import mean
import pandas as y
import numpy as x
A=int(input("enter the month number"))
city1=y.read_csv("seattle-weather.csv",index_col=0,parse_dates=True,dayfirst=True)
j=city1.groupby(y.Grouper(freq="M")).mean()
if A== 1 or 2  or 3 or 4 or 5 or 6:
    print("//////*****on season*****////")
    w=j.loc[y.date_range(start="2012-{0}".format(A),end="2016-{0}".format(A),freq="12M")]
    print(w)
    q=y.DataFrame(w)
    e=q.iloc[0:4,0]
    h=max(e)
    x=max(e)
    z=min(e)
    print("preciptitation=",h)
    if max(e)>75:
        print("RAINFALL WILL BE THERE")
    else:
        print("NO RAIN FALL")
    t=q.iloc[0:4,1]
    u=q.iloc[0:4,2]
    p=mean(t)
    f=mean(u)
    print("temp range=",f,"-",p)
    r=q.iloc[0:4,3]
    print("wind speed=",min(r),"-",max(r))
elif A== 7 or 8  or 9 or 10 or 11 or 12:
    print("//////*****off season*****////")
    w=j.loc[y.date_range(start="2012-{0}".format(A),end="2016-{0}".format(A),freq="12M")]
    print(w)
    q=y.DataFrame(w)
    e=q.iloc[0:4,0]
    h=max(e)
    x=max(e)
    z=min(e)
    print("preciptitation=",h)
    if max(e)>75:
        print("rainfall will be there")
    else:
        print("no rainfall")
    t=q.iloc[0:4,1]
    u=q.iloc[0:4,2]
    p=mean(t)
    f=mean(u)
    print("temprange",p,"-",f)
    r=q.iloc[0:4,3]
    print("maximum wind=",max(r))
    print("minimum wind=",min(r))
    print("windspeed=",min(r),"-",max(r))


    

