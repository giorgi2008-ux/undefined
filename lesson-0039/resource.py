# მინიმალური და მაქსიმალურის პოვნა
arr = [1,2,3,4,5,6]
def find_min_max(arr):
    smallest = arr[0]
    largest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest
print(find_min_max(arr))

print("---------------------------")

# ან დავწერთ min & max
Arr = [1,2,3,4]
def func(Arr):
    return max(Arr), min(Arr)
print(func(Arr))

print("---------------------------")

# წავშლოთ სფეისები
x = "linux magaria dzzan"
def no_space(x):
    return x.replace(" ", "") #replace ჩნაცვება,ჯერ ვწერთ რა ჩვანაცვლოთ და შემდეგ რით ჩვანაცვლოთ.
print(no_space(x))

print("---------------------------")

# შევკრიბოთ ელემენტები
a = [1,2,3,4,5]
def sum_array(a):
    total = 0
    i = 0

    while i < len(a):
        total += a[i]
        i += 1

    return total
print (sum_array(a))