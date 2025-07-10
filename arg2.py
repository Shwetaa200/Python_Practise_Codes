# default argument
def total_items(items = {},currency = "USD"):
    total_items= sum(items.values())
    print(f"Total no of items are: {total_items}")
    print(f"Currency is {currency}")
cart = {"apple" : 10 , "Banana": 20}
# total_items(cart , currency="INR") -->Highest Priority than USD then print INR
# total_items(cart)
total_items()