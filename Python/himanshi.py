from stringprep import c6_set

lst=[22,4,'himanshi']
print(lst)
lsst =[]
print(lsst)
print(len(lst))
print(lst*4)
print(lst[2])
lst.remove(22)
print(lst)
del (lst[1])
print(lst)
lst2=[1,2,3,4]
#st2.clear()
print(lst2)
print(max(lst2))
lst2.insert(2,45)
print(lst2)
#st2.sort(reverse=True)
print(lst2)
tpl=(1,2,45,"himanshi")
tpl1=(38,)
print(tpl)
print(tpl*5)
print(type(tpl))
tpl2=(1,22,22,1,22,1,45)
print(tpl2.count(22))
print(tpl2.index(22))
print(tpl2[0:2])
print(len(tpl2))
lst3=[1,2,3]
tpl3=tuple(lst3)
print(type(tpl3))
lst5=list(tpl3)
print(type(lst5))
s={1,2,3,4,"himanshi"}
print(type(s))
print(s)
s2={1,1,22,3,3,4}
print(s2)
s2.update([88,89])
print(s2)
s2.remove(22)
print(s2)


fr=frozenset(s2)
print(s2)
#create a list of countries of three countries
lst=["india","usa","canada"]
list.insert(1,"korea")
print(list)
list.remove("india")
print(list)
r=range(5)
print(r)
