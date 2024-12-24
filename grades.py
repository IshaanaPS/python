grades={}

num=int(input("enter the no of subjects: "))
for i in range(num):
    key=input("enter the subject: ")
    value=int(input("enter the mark: "))
    grades[key]=value

print(grades)

def average():
    s=sum(grades.values())
    result=s/num
    return result

r=average()
print(r)







