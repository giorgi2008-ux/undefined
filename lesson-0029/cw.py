array = [1, 2, 3, 3, 4, 5, 6, 7, 9,9,9,9,9,9,11,11,12,12]
array_index=array.index(9)
print(array_index)

print("----------------------")

def lomi():
    return"lekvi lomisa sworia"

lomi()
print(lomi())

print("----------------------")
def real_greeting(a,b,g):
    return  a + b + g
print(real_greeting(1,2,6))


def rel_greeting(name):

    return "hallo" + name

print(rel_greeting("gio"))

# ცვლადებს, რომლებიც იქმნება ფუნქციის გარეთ, გლობალური ცვლადები ეწოდება.
# გლობალური ცვლადების გამოყენება ყველას შეუძლია, როგორც ფუნქციების შიგნით, ასევე მის გარეთ.
# ხოლო თუ ჩვენ დავუწერთ global ამ შემთხვევაში ეს ცვლადი როგორც ფუნქიაში, ასევე ფუნქციის გარეთაც იმუშვებს.
def myfanc():
    global x
    x = "magali"
    print("gio aris ", x )
myfanc()

print("kola ar aris ", x)

# ასევე თ ცვლადს ფუნქციის შიგნით გარეთ შევქმნით,შეგვიძლია გამოვიყენოთ ფუნქციის შიგნით.

a = "magaria"

def Myfunc():
    print("goa ", a)

Myfunc()

# ფუნქციის შიგნით გლობალური ცვლადის მნიშვნელობის შესაცვლელად, ცვლადზე მიუთითეთ globalსაკვანძო სიტყვის გამოყენებით.
g = "hihi"

def my_func():
    global g
    g = "goa"
my_func()

print("we love ", g)
