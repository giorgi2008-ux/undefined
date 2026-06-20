x = y = ("gio")
print(x,y)

print("-------------")


fruits = ["f","g","c"]
e, b, c =fruits
print (e)
print (b)
print (c)

print("-------------")

# global ცვლადი local ცვლადი. გლობალური არის ფუნქციის გარრეთ და ლოკალური შიგნით
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print("-------------")

# თუ საკვამძ სიტყვას global ს გამმოვიყენებთ, ეს ცვლადი გლობალური გახდება და მის გარეთ გამოყენებასაც შევძლებთ
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print("-------------")
# ასევე შეგვიძლია global ის გამოყენებით ცვლადს მნიშვნელოდა შევუცვალოთ

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print("-------------")

# სამმაგი ბრჭყალებით შეგვიძლია str გადავიტანოთ ახალ ხაზზე
a1 = """python is the 
besshhh broo """
print(a1)

print('-----------------')
# გადაამოწმებს არის თუ არა free ტქსტში დაგვინრუნებს true / false
txt = "The best things in life are free!"
print("free" in txt)

# ვარიანტი 2
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


print('-----------------')
