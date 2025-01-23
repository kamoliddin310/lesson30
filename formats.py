import json
from pprint import pprint

f = open('people.json')

json_data = f.read()

users_list = json.loads(json_data)

# 1. Erkaklar va Ayollar sonini Hisoblab beradi Filter va lamba 
# funksiyasi orqali !!

# a = list(filter(lambda user: (user["gender"] == "Female"), users_list))
# print("Ayollar soni --> ", len(a))
# print("\n-----------------------------------------\n")
# b = list(filter(lambda user: user["gender"] == "Male", users_list))
# print("Erkaklar soni --> ", len(b))
# f.close()



# 2. Bu kodda Hindistonliklarni nechtaligini va ruyxatini chiqarib beradi chiqarib beradi !!!

# a = filter(lambda Indias: Indias["country"] == "India", users_list)
# print("Hindistonliklar")
# b = list(filter(lambda Indias: Indias["country"] == "India", users_list))
# print("\nJami Hindistonliklar soni --> ", len(b))
# print("\n")
# pprint(list(a))
# f.close()



# Bu kodda men 4 yoshli foydalanuvchi bulmaganligi sababki qushmadim
# oddiygina qilib 20 yoshdan kichiklarini chiqarib quya qoldim

# a = filter(lambda yosh:yosh["age"] <= 20, users_list)
# b = list(filter(lambda yosh:yosh["age"] <= 20, users_list))
# print("\n20 yoshdan kichik foydalanuchilar soni --> ", len(b))
# print("\n")
# pprint(list(a))
# f.close()



# BUnda muhandis kasbiga ega foydalanuvchilar ruyxati va 
# soni chiqarilib beriladi

a = filter(lambda muhandis: muhandis["job"] == "Engineer", users_list)
b = list(filter(lambda muhandis: muhandis["job"] == "Engineer", users_list))
print("\nMuhandislar soni --> ", len(b))
print("\n")
pprint(list(a))
f.close()

# bu kodda men asoosan filter(lamda) funksiyasidan foydalandim
# sababi bu usul orqali tez ishlash mumkinligi uchun