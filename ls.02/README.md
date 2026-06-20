ტექსტის ტიპი:	str
რიცხვითი ტიპები:	int, float, complex
თანმიმდევრობის ტიპები:	list, tuple, range
რუკების ტიპი:	dict
ნაკრების ტიპები:	set,frozenset
ლოგიკური ტიპი:	bool
ორობითი ტიპები:	bytes, bytearray, memoryview
არცერთი ტიპი:	NoneType

---------------------------------------------

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType


----------------------------------------------
# rendom დაპრინტავს რენდომად 1 დან 10 მდე

import random

print(random.randrange(1, 10))

---------------------------------------------
# ქასთნგი არის როცა მონაცემთა ტიპს ვცვლით

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

---------------------------------------------
# სტრიქონში შეგიძლიათ გამოიყენოთ ბრჭყალები, იმ პირობით, რომ ისინი არ ემთხვევა სტრიქონის გარშემო არსებულ ბრჭყალებს:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# სამმაგი ბრჭყალებით შეგვიძლია str გადავიტანოთ ახალ ხაზზე


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# ბევრი სხვა პოპულარული პროგრამირების ენის მსგავსად, Python-ში სტრიქონები უნიკოდის სიმბოლოების მასივებია.
# თუმცა, Python-ს არ აქვს სიმბოლოს მონაცემთა ტიპი, ერთი სიმბოლო უბრალოდ 1 სიგრძის სტრიქონია.
# კვადრატული ფრჩხილების გამოყენება შესაძლებელია სტრიქონის ელემენტებზე წვდომისთვის.

a = "Hello, World!"
print(a[1])

# გამოიტანს "e"e


for x in "banana":
  print(x)

# გამოიტანს 

b
a
n
a
n
a

# ფუნქცია len()აბრუნებს სტრიქონის სიგრძეს:

a = "Hello, World!"
print(len(a))
