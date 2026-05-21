class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

print('------------------------')
    
class person:
    def __init__(self,name,age):
        self.name1 = name # შეგვიძლია დავარქვათ რაც გვინდა, რითაც მერე მივწვდებით name-ს
        self.age1 = age   # და იგივეა age1-ს შემთხვევაში
    def __str__(self):  # შეგვიძლია შევქმნათ კიდევ ახალი ფუნქცია, სადაც გამოვიყენებთ name1-ს და age1-ს
        return f"name: {self.name1}, age: {self.age1}"

    def greet(self):
        return "hello hello"
new_person = person("gio",17)
print(new_person.name1)
print(new_person.age1)
print("----------------")
print(new_person)
print(new_person.greet())