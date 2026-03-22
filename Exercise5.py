# Maipulate date in a dictonary 
person = {"name":"Bhushan","age":28,"grade":"B"}
print(person)
#Add new kay value pair
person["address"] = "123 Main Street"

#update age
person["age"] = 34

#remove grade
if "grade" in person:
    del person["grade"]
    
print(person)