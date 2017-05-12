# -*- coding:utf-8 -*-
shoplist = ["apple", "mango", "carrot", "banana"]

print("I have", len(shoplist), "items to purchase")

print("These items are", end=" ")
for item in shoplist:
    print(item, end=" ")

print("\nI also have to buy rice")
shoplist.append("rice")
print("My shopping list is now", shoplist)
print("sort")
shoplist.sort()
print("Sortted list:", shoplist)
print("The first item", shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("I bought the ", olditem)
print("The last list:", shoplist)
