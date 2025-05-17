#zip
list1=["sag","ank","rot"]
list2=[23,27,34]
print(list(zip(list1,list2)))

print('-'*(50))

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print([[row] for row in zip(matrix)])
# print("the transpose is : ")
# print([[row] for row in zip(*matrix)])
# print("the transpose of transpose matrix is : ")
# print([[row] for row in zip(*[[row] for row in zip(*matrix)])])

print('-'*(50))

list3=[3,6,9]
list4=[2,8,3]
print([i*j for i,j in zip(list3,list4)])

print('-'*(50))
print('-'*(50))

#filter
list1=[1,2,3,4,5,6,7,8,9,10]
def is_even(n):
    return n%2==0

def is_odd(n):
    return n%2!=0

print("only the even numbers")
print(list(filter(is_even,list1)))
print('-'*(50))
print("only the odd numbers")
print(list(filter(is_odd,list1)))

print('-'*50)
print('-'*(50))


#lambda
new_num=lambda x,y : x*y
print(new_num(8,9))

num=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x%2!=0,num)))

print('-'*(50))
print('-'*(50))

#map
numbers = [1, 2, 3, 4, 5] 
squared_odd = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
print(squared_odd)