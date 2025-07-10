add=lambda n1,n2:n1+n2
print(add(10,20))

print("Lambda function in tuple")

add1 = lambda n1,n2:(n1+n2,n1-n2)
print(add1(10,20))
print("----------------------------------------------------------------")

print("nested lambda")
square = lambda n:n**2
modify=lambda func:lambda num:func(num)+num
var=modify(square)
print(var(int(input("Enter the number:"))))
print("----------------------------------------------------------------")


print("Lambda with if-else condition")

num1 = 20
num2 = 30

lambda n1,n2:n1 if num1<num2 else n2
print("Maximum number is : ",max(num1,num2))
print("----------------------------------------------------------------")


print("sorted using length")
print()
data = ["Shweta Date","Sakshi Pichad","Vrushali Shinde","Ashwini Bhagat"]
print(sorted(data,key=len))
print(sorted(data))
print()
print("*******************************************************************************")

print("Lambda with sorted")
print()
data = ["Shweta Date", "Sakshi Pichad", "Vrushali Shinde", "Ashwini Bhagat"]
# Sorting alphabetically
print(sorted(data))
# Sorting by length using lambda function
print(sorted(data, key=lambda x: len(x)))
print()
print("*******************************************************************************")


print("Soretd on the basis of surname")
print()
data = ["Shweta Date", "Sakshi Pichad", "Vrushali Shinde", "Ashwini Bhagat"]
# Sorting based on surname (last word in each name)
sorted_data = sorted(data, key=lambda x: x.split()[-1])
print(sorted_data)
print()
print("*******************************************************************************")

print("Using split function")
print()
data = ["Shweta Date", "Sakshi Pichad", "Vrushali Shinde", "Ashwini Bhagat"]

# Splitting names into first and last names
split_data = [name.split() for name in data]

# Sorting based on surname (last word in each name)
sorted_data = sorted(split_data, key=lambda x: x[-1])

print(sorted_data)
