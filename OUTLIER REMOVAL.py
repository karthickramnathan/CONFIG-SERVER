#create a function
#w=df['column']
#a= df
def outlier(w,a):
q1 = w.quantile(0.25)
q3 = w.quantile(0.73)
iqr = q3-q1
low = q1-(1.5*iqr)
high = q3 + (1.5*iqr)
y = np.array(w[(w<low) | (w>high)])
a[w.isin (y)]=a.median()
return a

