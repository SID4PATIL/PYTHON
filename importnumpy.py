import numpy as np
import pandas as pd
a=np.array([[5,1],[2,3]])
b=np.array([[1,2],[7,8]])

c=np.dot(a,b)

print(pd.__version__)
products = ['A', 'B', 'C', 'D']
print(type(products))

start_date_deposits = pd.Series({
    '7/4/2014'   : 2000,
    '1/2/2015'   : 2000,
    '12/8/2012'  : 1000,
    '2/20/2015'  : 2000,
    '10/28/2013' : 2000,
    '4/19/2015'  : 2000,
    '7/4/2016'   : 2000,
    '4/24/2014'  : 2000,
    '9/3/2015'   : 4000,
    '7/25/2016'  : 2000,
    '5/1/2014'   : 2000,
    '3/29/2013'  : 2000,
    '10/3/2014'  : 2000,
    '9/18/2015'  : 2500
})

#print(start_date_deposits)



arr=np.array([[100,20],[300,40]])

print(arr)
print("\n")
print(np.insert(arr,[0,2],[90,00],axis=1))

ui=np.sort(arr[0:1])

print(ui)


print()
yt=pd.read_csv("C:/Users/SID/Downloads/annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv")


print(yt)
print()
print()
print()
print()
print(yt.head(10))
print()
print()
print()
print()
print(yt.tail(10))
print()
print()
print()
print(yt.info())
print()
print()
print()
print()
print(yt.describe())
print()
print()
print()
print()
print(yt.isnull())
print()
print()
print()
print()
print(yt.isnull().sum())

