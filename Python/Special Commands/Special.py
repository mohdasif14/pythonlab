# a=None
# print(a)
#
# print("Java is a \ngood language")
# print("Java is a \tgood language")
#
# print("My name is \"DR Doom\"")
#
# # a=10
# # print(a)
# # del (a)
# # print(a)
#
# #del for strings
#
# S = "abcdefg"
# del(s[1])
# print(s)
from os import remove

# a = 20
# b = 20
# print(id(a),id(b))

# a = 20
# b = 20
# p = 30
# print(id(a),id(p))

lst = [1,2,3,"apple"]
lst.remove("apple")
print(lst)

bytesnew = bytes(lst)

b1 = bytearray(bytesnew)