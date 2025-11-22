def func(s):
    result = []
    word = ""
    for i in s:
        if i == " ":
            result.append(word)
            word = ""
        else:
            word += i
    result.append(word)
    return result
print(func("linux dzzan magaria"))

print("-----------------------")


def fake_bin(x):
    res = 0
    for i in x:
        if int(x) > 5:
            res += "1"
        else:
            res += "0"
    return res
print(fake_bin(237645))
