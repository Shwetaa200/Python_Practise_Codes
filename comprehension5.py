str1= "coding"
my_dict = {}
for char in str1:
    my_dict[char.upper()]=(ord(char),ord(char.swapcase()))
print(my_dict)

# Dictionary comrehension
print({char.upper(): (ord(char), ord(char.swapcase())) for char in str1})
