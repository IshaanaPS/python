str=input("enter the string")
flag=0
l=len(str)-1

for i in range(l//2):
    if str[i]=='(' and str[l-i]!=')':
        flag=1
        break
    elif str[i]=='{' and str[l-i]!='}':
        flag=1
        break
    elif str[i]=='[' and str[l-i]!=']':
        flag=1
        break
    else:
        continue

if flag==0:
    print("palindrome")
else:
    print("not palindrome")

  
