data = [23,45,35,42,20,36,37,98,100]

def even(num):
    if num%2==0:
        return True
    else:
        return False
    
filterd_obj = filter(even,data)
print(filterd_obj)
print(type(filterd_obj))
print(list(filterd_obj))
