person ={
    # kay | value  
    "name":"gio",
    "age": 17,
    "height": "1,95cm" 
}
inf = person["age"]
print(inf)

# განახლება
person["age"] = 14

# დამატება
person["county"] = "Georgia"


# წაშლა
del person["county"]

print(person)

for key in person:
    print(person[key])
    