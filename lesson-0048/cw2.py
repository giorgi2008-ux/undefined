def func(g):
    r = ""
    for i in range(len(g)):
        r += g[i].upper() + g[i].lower() * i + "-"
    return r[:-1]
print(func("func"))


print("--------------------------")


def name(n):
    res = ""
    for i in range(len(n)):
        res += n[i].upper() + n[i].lower() * i + "-"
    return res[:-1]
print(name("gio"))


print("--------------------------")

def fruit(f):
    result = ""
    for i in range(len(f)):
        result += f[i].upper() + f[i].lower() * i + "-"
    return result[:-1]
print(fruit("apple")) 


print("--------------------------")



def car(brand):
    R = ""
    for i in range(len(brand)):
        R += brand[i].upper() + brand[i].lower() * i + "-"
    return R[:-1]
print(car("bmw"))
