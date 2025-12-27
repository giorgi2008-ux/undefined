def maskify(cc):
    if len(cc) <= 4:
        return cc
    a = "#" * (len(cc) - 4)
    return a + cc[-4:]
print(maskify("2374667236"))


print("--------------------------")


def Password(p):
    if len(p) <= 2:
        return p
    a = "#" * (len(p) - 2)
    return a + p[-2:]
print(Password("2937467"))


print("--------------------------")


def func(gg):
    if len(gg) <= 5:
        return gg
    bb = "#" * (len(gg) -5 )
    return bb + gg[-5:]
print(func("5948275"))


print("--------------------------")


def code(c):
    if len(c) <= 4:
        return c
    a = "#" * (len(c) - 4)
    return a + c[-4:]
print(code("54001046578"))
