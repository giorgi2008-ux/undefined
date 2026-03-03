name = input("what's ur name: ")
print(name)

print("------------")

n = input("სახელი:")
s = input("გავრი:")
print(f"გამარჯობა, {n} {s}")


print("------------")


num1 = int(input("შიყვანე რიცხვი:"))
num2 = int(input("შიყვანე კიდევ ერთი:"))
print(num1 + num2)
print(num1 * num2)


print("------------")

age = int(input("ასაკი:"))
a = (2026 - age)
print(f" თქვენ დაიბადეთ {a} წელს")

print("------------")


passs = input("შეიყვანე პაროლი:")
print(len(passs))


print("------------")


celsius = float(input("შეიყვანე ტემპერატურა ცელსიუსში: "))
fahrenheit = ((celsius * 1.8) + 32)
print("ტემპერატურა ფარენჰეიტში არის:", fahrenheit)
