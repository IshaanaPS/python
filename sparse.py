def read_mat():
    #c=int(input("enter the number of rows: "))
    #r=int(input("enter the number of coloumns: "))

    matrix={}
    print("enter the sparse representation: ")
    while True:
        entry=input().split()
        if len(entry)==0:
            break
        row,col,val=map(int,entry)
        matrix[(row,col)]=val
    return matrix

def display_mat(matrix,r,c):

    for i in range(r):
        for j in range(c):
            print(matrix.get((i,j),0),end=" ")
        print()


matrix=read_mat()
rows=int(input("enter the number of rows: "))
cols=int(input("enter the number of coloumns: "))
display_mat(matrix,rows,cols)
