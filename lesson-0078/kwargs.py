# **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print("---------------------")

# 
def my_function(**kwargs):
  print("Type:", type(kwargs))
  print("First argument:", kwargs["name"])
  print("Second argument:", kwargs["age"])
  print("Third argument:", kwargs["city"])
  print("All arguments:", kwargs)

my_function(name="Emil", age=30, city="New York")

print("---------------------")

# **kwargs-ის გამოყენება სხვადასხვა რაოდენობის არგუმენტების მისაღებად, key=value სახით
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

print("---------------------")

# შეგვიძლია list-ის ელემენტები გამოვიყენოთ როგორც არგუმენტები 
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

print("---------------------")

# შეგვიძლია dictionary-ის ელემენტები გამოვიყენოთ როგორც არგუმენტები
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
