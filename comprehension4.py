# Syntax 04 :: [expression for variable in iterable if-else condition]
nums = [1,2,3,4,5,6,7,8,9]
mylist = []
for num in nums:
    if(num%2 == 0):
            mylist.append(num**2)
    else:
            mylist.append(num**3)
print(mylist)

# List comprehension
print([num**2 if num%2==0 else num**3 for num in nums])
