def binary(decimal):
    b=bin(decimal)
    return b

def hexadecimal(decimal):
    h=hex(decimal)
    return h

def octadecimal(decimal):
    o=oct(decimal)
    return o

num=int(input("enter the number to convert: "))

def options():
    print("1.binary\n")
    print("2.octadecimal\n")
    print("3.binary\n")
    ch=int(input("enter your choice: "))
    if ch==1:
        result=binary(num)
        print('the binary conversion of',num,"is",result)
    elif ch==2:
        result=hexadecimal(num)
        print('the hexadecimal conversion of',num,"is",result)
    elif ch==3:
        result=octadecimal(num)
        print('the binary conversion of',num,"is",result)

options()
        
  
