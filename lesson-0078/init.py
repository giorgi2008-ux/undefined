
# class-ის შექმნა, __init__ მეთოდი არის კონსტრუქტორი, რომელიც იძახება ობიექტის შექმნისას
class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

res = person1("giorgi",20)

print(res.name)
print(res.age)

       