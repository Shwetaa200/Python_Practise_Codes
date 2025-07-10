# convert data into json file
import json
sports = ["Cricket", "Kabbaddi", "Badminton" , "Kho-Kho"]
data =dict(list(enumerate(sports,1)))
f = open("data.json" , "w")
json.dump(data,f)
f.close