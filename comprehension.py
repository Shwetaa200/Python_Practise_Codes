# Comprehension --> To write a compact code 
# List comprehension
# Syntax 02 :: [expression for variable in iterable]

nums = [1,2,3,4,5,6,7,8,9]
mylist = []
for num in nums:
    mylist.append(num**2)
print(mylist)

# List comprehension
print([num**2 for num in nums])
