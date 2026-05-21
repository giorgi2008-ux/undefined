class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
    def greeting(self):
        return f"hello {self.name}"

class person2(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.__init__(self,name,age)


new_person = Person("gio",17)
print(new_person)
print(new_person.greeting())

print("----------------------------")

new_person2 = person2("luka",18)
print(new_person2)
print(new_person2.greeting())


print("----------------------------")


class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # private method
p1 = person("giorgi",17)
print(p1.__age) #ამას ვერ დავპრინტავთ რადგან private method-ია.
print(p1.name)