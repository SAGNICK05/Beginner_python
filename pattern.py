# n=int(input("enter the no of rows:"))
# for i in range (1,n+1,1):
#     for j in range (1,i,1):
#         if(j==1 or j==i):
#             print("*",end=" ")
#         else:
#             print(" ",end="")
#     print()

# to print this pattern
# *
# * *
# *  *
# *   *
# *    *
# * * * *

n=int(input())
for i in range (1,n,1):
    for j in range (1,n+1,1):
        if(i==j or j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
for i in range(1,n+1):
    print("*",end=" ")