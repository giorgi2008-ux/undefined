def reverse_words(text):
    res = text.split(" ")
    res2 = []

    for i in res:
        res2.append(i[::-1])

    return " ".join(res2)
print(reverse_words("giorgi var brat"))


print("-----------------------------")


def reverse(text):
    res = text.split(" ")
    return res
print(reverse("gi or gi"))
