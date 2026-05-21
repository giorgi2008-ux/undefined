# text = "Python is very cool and python is very easy"
# def func(text):
#     res = []
#     x = text.split()
#     for i in x:
#         if i not in res:
#             res.append(i.lower())
#         a = res.count("python")
#         b = res.count("is")
#         c = res.count("very")
#         d = res.count("cool")
#         e = res.count("and")
#         f = res.count("easy")
        
# print(func(text))

text = "Python is very cool and python is very easy"

# 1. ტექსტის გადაყვანა პატარა ასოებად
lower_text = text.lower()

# 2. ტექსტის დაშლა სიტყვების ლისტად
words_list = lower_text.split()

# 3. ცარიელი ლისტის შექმნა
unique_words = []

# 4 & 5. ციკლით გადავლა და უნიკალური სიტყვების დამატება
for i in words_list:
    if i not in unique_words:
        unique_words.append(i)

# 6 & 7. თითოეული უნიკალური სიტყვის დათვლა და დაბეჭდვა
print("სიტყვების რაოდენობა:")
for i in unique_words:
    word_count = words_list.count(i)
    print(f"{i} - {word_count}")

# 8. join() მეთოდის გამოყენება სიტყვების გასაერთიანებლად
joined_words = " | ".join(unique_words)

print("\nგაერთიანებული ლისტი:")
print(joined_words)

print("----------------")

def analyze_text(text):
    # პატარა ასოებად
    text = text.lower()
    
    # სიტყვებად დაყოფა
    words = text.split()
    
    # უნიკალური სიტყვები
    unique_words = []
    
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    # დათვლა და დაბეჭდვა
    for word in unique_words:
        count = words.count(word)
        print(f"{word} - {count}")
    
    # join
    result = " | ".join(unique_words)
    print(result)


# გამოძახება
text = "Python is very cool and python is very easy"
analyze_text(text)