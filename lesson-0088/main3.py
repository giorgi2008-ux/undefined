arr = [1,2,3,4,5,6,7,8,9,10]
def func(arr):
    even = []
    odd = []

    for i in (arr):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return f'even:{even}, odd:{odd}'
print(func(arr))


print("----------------------------------------")

arr2 = [2,3,4,5]
def func2(arr):
    res = []
    for i in arr:
        res.append(i*2)

    return res
print(func2(arr2))
    
