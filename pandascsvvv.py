import numpy as np
import pandas as pd

dis={

    "A" : [1,2,3,4,4,5,6,7],
    "B" : [1,2,3,4,4,5,6,9],
    "C" : [1,2,3,4,4,5,0,5],
    "D" : [1,2,3,4,4,5,6,0]

}

a=pd.DataFrame(dis)

a.to_excel("G:/VS CODE/tcarp/trial3.xlsx",index=False,header=["sid","shru","pat","huu"])

d=pd.read_excel("G:\\VS CODE\\tcarp\\moviez.xlsx",nrows=5)

#print(d)

p=pd.read_excel("G:\\VS CODE\\tcarp\\moviez.xlsx")

p.to_excel("G:/VS CODE/tcarp/trial4.xlsx",index=False)
#print(p)
w=p.describe()

#print(w.max())

u=p.to_numpy()

#print(u[1][1])


q=p.sort_index(axis=0,ascending=False)



#print(q)

aa=p.loc[:,["title","budget","revenue"]]

#print(aa.iloc[2,2])
uu=aa.min
vv=aa.max
#print(uu)
np.asarray(uu)


#print(p)

#print(p.dropna())
 

re=pd.read_excel("G:\\VS CODE\\tcarp\\trial3.xlsx")
print(re)

print(re.replace(0,method="ffill"))
#print(re)




