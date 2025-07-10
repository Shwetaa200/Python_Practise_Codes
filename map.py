names  = ['Shweta','Sakshi','Vrushali','Ashwini']

def find_length(names):
    return len(names)

mapped_obj = map(find_length,names)
print(mapped_obj)
print(type(mapped_obj))
print(list(mapped_obj))

# Square
arr = [2,3,4,5,9,8]

def square(n):
    if n%2!=0:
        return n**2
    else:
        return n

mapped_obj = map(square,arr)
print(mapped_obj)
print(type(mapped_obj))
print(list(mapped_obj))

# Addition
num1 = [10,20,30]
num2 = [2,3,4]

def add1(a,b):
    return a+b

mapped_obj = map(add1,num1,num2)
print(list(mapped_obj))