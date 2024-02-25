lis=[9,8,7,6,5,4,2,3]
lis.sort()
#print(lis)

lis.reverse()

#print(lis)




qns=["kuch khaya aapne?","Dawai li aapne?","Happy Happy?"]
maaa_ka_ans="haan kuch khaya"
beta_kya_socha=maaa_ka_ans.split(" ")
list(beta_kya_socha)
for i in range (0,3):
    print("beta ka qns" + "-------"  + qns[i])
print("\n")
print("maa ka uttar --------"  ,  beta_kya_socha)
print("\n")
print("beta ko kuch samaj nahi aya")
print("\n")
beta_kya_socha.reverse()
print("what beta deciphered -------" , beta_kya_socha)
print("\n")
print(qns[0])
print(beta_kya_socha[0] + "\n")
print(qns[1])
print(beta_kya_socha[1] + "\n")
print(qns[2])
print(beta_kya_socha[2] + "\n")




import pandas as pd

re=pd.read_excel("G:\\VS CODE\\tcarp\\trial3.xlsx")
#print(re)
#print(re.fillna(100))