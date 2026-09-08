# To initialize a list
friends =["apple","orange",5 ,343.22,False,"Anurag"]

#append method(will add new value to the end of the list)
friends.append("Anurag")
print(friends)

#sort method (will sort the numbers)
l1=[1,22,99,23,5,66,7]

l1.sort()
print(l1)


#Reverse Method
l1.reverse()            #will reverse the list 
print(l1)



#insert method
l1.insert(4,333)        #first give the index and then the reqired object
print(l1)



#pop method

# l1.pop(2)              will delete the the value at 2nd index
# value=l1.pop(3)
# print(value)           will also return the same value of the poped element

print(l1.pop(2))        #will give the poped/deleted value of the list
print(l1)               #will print the list poping/deleting the valyue of the targeted index

