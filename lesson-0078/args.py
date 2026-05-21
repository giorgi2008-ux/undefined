# *args

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("Third argument:", args[2])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

print("---------------------")

x = "Hello"
y = ("Emil", "Tobias", "Linus")
def my_function(x, y):  
  for i in y:
    print(x, i)

print("---------------------")

my_function(x,y )  
# იგივეა რაც 
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


print("---------------------")

# *args-ის გამოყენება სხვადასხვა რაოდენობის არგუმენტების მისაღებად
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


print("------------------------")

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1)) 