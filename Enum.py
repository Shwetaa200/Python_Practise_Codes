sports = ["Cricket", "Kabbaddi", "Badminton" , "Kho-Kho"]

enum_obj = enumerate(sports,1)

print(enum_obj)
print(type(enum_obj))

print(list(enum_obj))

for pos,ele in enumerate(sports):
    print(f"{pos}:{ele}")
# convert into dictionary
print(dict(list(enumerate(sports,1))))