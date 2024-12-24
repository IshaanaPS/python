num=int(input("enter a number: "))
div=[]

for i in range(1,num+1):
    if num%i==0:
        div.append(i)

print(div)
