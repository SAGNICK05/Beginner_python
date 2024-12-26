str=input("enter the string")
str=str.lower()
if str==str[::-1]:
    print("it is palindrome")
else:
    print(" it is not palindrome")
    
# s=input("enter the string : ")
# high=len(s)-1
# low=0
# c=0
# while(low<high):
#     if(s[low]!=s[high]):
#         print("it is not palindrome")
#         c=1
#         break
#     else:
#         low+=1
#         high-=1
# if(c==0):
#     print("it is palindrome")
