from pydoc import describe
from statistics import median
from cv2 import mean
import numpy as np
import pandas as p
import matplotlib.pyplot as plt
store=p.read_csv("SampleSuperstore.csv")
print(store.isnull().sum())
print("*****outlierhandling********")
store["Quantity"].plot.box()
plt.show()
i=store["Quantity"]>9.99
store["Quantity"][i==True]=(store["Quantity"]).median()
store["Quantity"].plot.box()
plt.show()
print("***************Quantityhandeled*****************")
store["Discount"].plot.box()
plt.show()
w=store["Discount"]>0.59
store["Discount"][w==True]=(store["Discount"]).median()
store["Discount"].plot.box()
plt.show()
print("***************Discounthandeled*****************")
store["Sales"].plot.box()
plt.show()
y=store["Sales"]>0.4
store["Sales"][y==True]=(store["Sales"]).median()
store["Sales"].plot.box()
plt.show()
print("***************Sales handeled*****************")
print(store.describe())
# store.plot.box()
# plt.show()
a=store.groupby(["Category","Sub-Category"])["Sales"].sum().plot(kind="bar")
a.set_ylabel("Sales")
plt.show()
b=store.groupby(["Category","Sub-Category"])["Quantity"].sum().plot(kind="bar")
b.set_ylabel("Quantity")
plt.show()
c=store.groupby(["Segment"])["Sales"].sum().plot(kind="pie")
plt.show()
d=store.groupby(["State"])["Profit"].sum().plot(kind="bar")
d.set_ylabel("Profit")
plt.show()

