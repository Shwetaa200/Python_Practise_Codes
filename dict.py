# properties of dictionary
# 1.unordered
# 2.mutable
# 3.indexed
# 4.cannot contain duplicate keys
marks ={
    "Shweta": 97,
    "Saurav": 99,
    "Gaurav": 100   #100:"Gaurav"
}
print(marks,type(marks))
print(marks['Gaurav'])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Shweta":98,"Pravin":95})
print(marks)
print(marks.get("Saurav"))