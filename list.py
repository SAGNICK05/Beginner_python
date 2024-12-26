#lists are mutable

l=[5,8,9,4,6,2]
print(l)
print(l[2])
print(l[-3])#3rd last value
print(l[-5])#5th lsst value

#list functions
#append() - adds an element at the end of the list
l.append(10)
print("after appending",l)

#insert() - adds an element at a specified position in the list
l.insert(2, 20)
print("after inserting",l)

#remove() - removes the first occurrence of the specified element from the list
l.remove(20)
print(l)

#pop() - removes the element at the specified position in the list and returns the removed element
print(l.pop())
print(l)
print(l.pop(2))
print(l)

#del - removes the element at the specified position in the list
del l[2]
print(l)

#sort() - sorts the list in ascending order
l.sort()
print(l)

#reverse() - reverses the list
l.reverse()
print(l)

#in function
print(5 in l)

#count()
l.append(8)
print(l.count(8))

#extend
l.extend([1,2,3,4,5])
print(l)


#index()
print(l.index(6))
# print(l.index(2,4,7))
# print(l.index(2,5,9))

#max - returns the largest item in the list
print(max(l))
# min - returns the smallest item in the list
print(min(l))
#sum - returns the sum of all items in the list
print(sum(l))

l=[1,12,3,4,5]
print(l*2)

