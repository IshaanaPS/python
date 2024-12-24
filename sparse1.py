def read_sparse():
  r=int(input("enter the umber of rows: "))
  c=int(input("enter the number of cols: "))
  
  matrix={}
  print("enter the sparse representation: ")
  while True:
     entry=input().split()
     if len(entry)==0:
        break
     row,col,val=map(int,entry)
     matrix[(row,col)]=val
  return matrix

def display_mat(matrix,c,r):
   for i in range(r):
      for j in range(c):
         print(matrix.get((i,j),0),end=" ")
      print()