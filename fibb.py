def fib(n):
    if n<0:
        print("invalid input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
num=int(input("enter the number :"))
a=fib(num)
print(a)
    

    
    
