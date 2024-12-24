import math as m

def binetFormula(n):
    phi=(1+m.sqrt(5))/2
    return int((pow(phi,n)-pow(-phi,-n))/m.sqrt(5))


n=int(input("enter value"))
for i in range(n):
    print(binetFormula(i))
