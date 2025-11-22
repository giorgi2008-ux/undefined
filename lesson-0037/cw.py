# def func(b):
#     return (b**2)
# func(2)
# func(3)
# func(4)
# func(5)
# func(6)


arr=[-1,5,7,-4,9]
def func(arr):
    sum = 0
    for i in range (len(arr)):
        if arr[i] > 0:
            sum = sum + arr[i]
    return sum
print(func(arr))


print("------------------------")


x =[5,-4,6,8,-1,-2,-4,7]
def y(x):
    number = 0
    for i in range(len(x)):
        if x[i] > 0:
            number = number + x[i]
    return number
print(y(x))


print("------------------------")


num =[12,34,-54,76]
def plus(num):
    num1 = 0
    for i in range(len(num)):
        num1 += num[i]
    return num1
print(plus(num))