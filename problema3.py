from math import log
m=int(input("introduceti numarul m: "))
n=int(input("introduceti numarul n: "))
i=log(n,m)
l=int(i)
if i-l==0:
    print ("n este putere al lui m")
else:
    print("n nu este putere al lui m")
