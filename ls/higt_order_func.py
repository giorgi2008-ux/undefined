
# first class function
def is_even(x):
    if x % 2 == 0:
        return x
    return "this is not even"


x = is_even
print(x(4))


# higher order function
def h_func(func, x):
    return func(x)  


def w(x):
    return x + 1


y = h_func(w, 4)
print("this is return value ->", y)  























def func(moqmedeba,cifri):
    return moqmedeba(cifri)


def func2(cifri):
    return cifri + 1

def func3(cifri):
    return cifri * 2

def func4(cifri):
    return cifri / 2

res = (func(func2, 1))
res2 = (func(func3, 10))
res3 = (func(func4, 10))
print(f"am kod agar davwer {res} dge")
print(f"ramdenia es ricxvi {res2}")
print(f"{res3} da es ramdenia? ")






