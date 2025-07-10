import copy
mylist = [[1,2,3],[4,5],[6,'a']]
print("id of mylist: ",id(mylist))
print("id of first element: ",id(mylist[0]))
print("id of first element: ",id(mylist[1]))
print("id of first element: ",id(mylist[2]))
newlist = mylist
newlist = copy.copy(mylist)  #Shallow copy
print(newlist)
print("------------------------------------------------------------------")
newlist = copy.deepcopy(mylist) #Deepcopy
print(newlist)
print("----------------------------------------------------------------------")
print("id of newlist: ",id(newlist))
print("id of first element: ",id(newlist[0]))
print("id of second element: ",id(newlist[1]))
print("id of third element: ",id(newlist[2]))

newlist[0][2] = "Hello"
print(newlist)


