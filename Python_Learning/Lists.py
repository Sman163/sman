myList = [1,2,"sman",True,10.5]
print(type(myList[0]))
print(type(myList[2]))
print(type(myList[3]))
print(type(myList[-1]))
#=========================================
print(myList[:3])
print(myList[2:])
print(myList[1:4])
print(myList[::2])
#========================================
myList[0] = 5
myList[-2] = False
myList[2] = "7arakat"
print(myList)
myList[0:3] = [4,6,"john"]
print(myList)
#=================== Lists Methods
#1 append()

mynewFriends = ["Ahmed","Osama","Alaa","Waled"]
mynewFriends.append("Youseff")
print(mynewFriends)
myOldFriend = ["salah","abdallah"]
mynewFriends.append(myOldFriend)
print(mynewFriends)
print(mynewFriends[5][1])

#2 extend()

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#3 remove() => its Just Remove the last index of the List
#4 sort() => its Sort the numerical value of the List or sorts alphabetically (reverse=True) => if u want reverse list

#5 reverse() => its reverse the actuall list whatever it is ["g" , "4"] => ["4" , "g"]
#6 clear() => delete all the element in the list
#7 copy() => make a copied list from the main list (note: any change that happend to the main list doesn't affect on the main list)
#8 insert(index , elemnt value) => insert an element in an a specific index in the list
#9 index() =>  declare the index in the list from a givin element if exists
#10 pop() => call the element from its index
#11 count() => count the repeated value of an index