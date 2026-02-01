

person = {
    "name":"gio",
    "age":"17"
}
print(person["name"])

print("------------------")

# შეგვიძლია გამოვიტანოთ მხოლოდ key
for key in person:
    print(key)

print("------------------")

# შეგვიძლია გამოვიტანოთ მხოლოდ value
for value in person.values():
    print(value)

print("------------------")

# შეგვიძლია გამოვიტანოთ მხოლოდ value & key ერთად
for key,value in person.items():
    print(key,"-->",value)

print("------------------")

# შეგვიძლია ლისტში თითოეულ dictionary-ს გადავუაროთ და ამ შემთხვევაში გამოვიტანოთ ორივე dictionary-ა name-ც და age-ც.
people =[
    {"name":"giorgi","age":17},
    {"name":"gio","age":17}
]

for i in people:
    print(i["name"],i["age"])

print("------------------")

# if + loop 
ppl = [
    {"name": "gio", "age": 17},
    {"name": "nika", "age": 18},
    {"name": "luka", "age": 19}
]

for i in ppl:
    if i["age"] >= 18:
        print(i["name"], "is an adult")
