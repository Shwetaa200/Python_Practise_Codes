def f_c(f):
    return 5*(f-12)/9
f = int(input("Enter the temp in F: "))
c=f_c
print(f"{round(c,2)} degC")