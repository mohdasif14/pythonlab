# # --- Decorator Function ---
# # Yeh decorator function hai jo kisi function ko input ke taur par leta hai,
# # uske result ko modify karta hai aur updated result ko return karta hai.
#
# def decor(fun):
#     result = fun() * 2  # `fun()` function ko call karke uska output lete hain aur usse 2 se multiply karte hain
#     return result  # Modified result return karte hain
#
# # Simple function jo ek number return karta hai
# def num():
#     return 25
#
# # `decor` function ko `num` function ke saath use karte hain aur output print karte hain
# print(decor(num))  # Output: 50 (kyunki num() ka output 25 hai aur decor uska double karta hai)
#
#
# # Ek simple function `hello` banaya jo kisi naam ko greet karta hai
# def hello(name):
#     return 'Hello ' + name  # Name ke sath 'Hello ' add karta hai
#
#
# # `hello` function ko call karke "Asif" naam pass kar rahe hain
# print(hello("Asif"))  # Output: Hello Asif
#
#
# # --- Decorator Function ---
# # Yeh decorator function hai jo kisi function ko modify kar sakta hai
# def decor(fun):
#     # `fun` function ko call karke result2 mein uska output store karte hain
#     result2 = fun("Asif")
#
#     # result2 ke sath ek additional message add karte hain
#     result2 = result2 + " How Are You"
#
#     # Modified result ko return karte hain
#     return result2
#
#
# # `decor` function ko `hello` function ke saath use karke modified output lete hain
# answer = decor(hello)
# print(answer)  # Output: Hello Asif How Are You


# --- Keywords List in Python ---
# Python ke keywords ko import karne ke liye `keyword` module ka use karte hain
import keyword

# `kwlist` Python ke keywords ka list hai, jo `keyword` module se milta hai
print(keyword.kwlist)  # Yeh line saare Python keywords ko print karegi

# Keywords ki total length ya count ko check karte hain
print(len(keyword.kwlist))  # Keywords kitne hain yeh batata hai
