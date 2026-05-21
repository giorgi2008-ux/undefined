# a = "gio"
# def func(a):
#     return a
# print(func(a))

# print("------------")

# def func(i):
#     return i
# print(func("gio"))

#დააბრუნებს ერთი და იმავე პასუხს.


    


# price = "1234"
# def to_currency(price):
#     g = ""
#     for i in price:
#       g += i
#     return g   
# print(to_currency(price))  

lst = [1,2,3]
def invert(lst):
    res =[]
    for i in lst:
        if i > 0:
            res.append(-i)
    return res
print(invert(lst))