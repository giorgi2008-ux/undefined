# 1) ანას აქვს 10 ლარი ანგარიშზე 

# თუ გადაიხდის 5 ლარს იყიდს ვაშლს

# თუ გადაიხდის 2 ლარს იყიდს სხალი

# თუ გადაიხდის იმაზე მეტს ვიდრე აქვს ანგარიშზე მაგ შემთხევაში დაგვიწერს რომ არ გვაქვს ბალანზე თანხა!


bouy = 2
if bouy  == 5:
    print("ნაყიდია ვაშლი")
elif bouy  == 2:
    print("ნაყიდია მსხალი")
else:
    print("არ გვაქვს ბალანსზე თანხა")
 



anna_money=10
buy=7
if buy == 5:
    anna_money = anna_money-5
    print("შენ შეიძინე ვაშლი და დაგრჩა",anna_money,"ლარი")
elif buy == 7:
    anna_money = anna_money-7
    print("შენ იყიდე მსხალი და დაგრჩა",anna_money,"ლარი")




anna_money=int(input("რამდენი ლარი გაქვს ანგარიშზე?: "))
buy=int(input("რამდენ ლარს დახარჯავ?: "))
if buy == 5:
    anna_money = anna_money-5
    print("შენ შეიძინე ვაშლი და დაგრჩა",anna_money,"ლარი")
elif buy == 7:
    anna_money = anna_money-7
    print("შენ იყიდე მსხალი და დაგრჩა",anna_money,"ლარი")
else:
    print("შენ შეიძინე სხავ ნივთი")