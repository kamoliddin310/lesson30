import json
from pprint import pprint
# 1. Erkaklar va Ayollar sonini Hisoblab beradi Filter va lamba funksiyasi orqali
def Hisoblash(w: str, e: str):
    a = list(filter(lambda user: (user["gender"] == w), users_list))
    print("Ayollar soni --> ", len(a))
    print("\n-----------------------------------------\n")
    b = list(filter(lambda user: user["gender"] == e, users_list))
    print("Erkaklar soni --> ", len(b)) 

# 2. Bu kodda Hindistonliklarni nechtaligini va ruyxatini chiqarib beradi chiqarib beradi
def India(h):
    a = filter(lambda Indias: Indias["country"] == h, users_list)
    print("Hindistonliklar")
    b = list(filter(lambda Indias: Indias["country"] == h, users_list))
    print("\nJami Hindistonliklar soni --> ", len(b))
    print("\n")
    pprint(list(a))

# 3.Bu kodda 20 yoshdan katta foydalanuvchilarni nechtaligi va ruyxatini chiqarib beradi
def count(h: int):
    a = filter(lambda yosh:yosh["age"] <= h, users_list)
    b = list(filter(lambda yosh:yosh["age"] <= h, users_list))
    print("\n20 yoshdan kichik foydalanuchilar soni --> ", len(b))
    print("\n")
    pprint(list(a))

# 4.Bunda muhandis kasbiga ega foydalanuvchilar ruyxati va soni chiqarilib beriladi
def kasbi(d: str):
    a = filter(lambda muhandis: muhandis["job"] == d, users_list)
    b = list(filter(lambda muhandis: muhandis["job"] == d, users_list))
    print("\nMuhandislar soni --> ", len(b))
    print("\n")
    pprint(list(a))

f = open('people.json')
json_data = f.read()
users_list = json.loads(json_data)


# 1. Erkaklar va Ayollar sonini Hisoblab beradi Filter va lamba
# funksiyasi orqali !!

# w = "Female"
# e = "Male"
# Hisoblash(w, e)
# f.close()

# 2. Bu kodda Hindistonliklarni nechtaligini va ruyxatini chiqarib beradi chiqarib beradi !!!

# a = "India"
# India(a)
# f.close()


# Bu kodda 20 yoshdan katta foydalanuvchilarni nechtaligi va ruyxatini chiqarib beradi
# a = 20
# count(a)
# f.close()

# Bunda muhandis kasbiga ega foydalanuvchilar ruyxati va soni chiqarilib beriladi

a = "Engineer"
kasbi(a)
f.close()

# bu kodda men asoosan filter(lamda) funksiyasidan foydalandim sababi bu usul orqali dastur tez ishlash mumkin deb uyladim va kam kod
