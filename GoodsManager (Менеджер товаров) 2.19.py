goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Новый фрукт: ')
price = input('Цена: ')
new_good = []
new_good.append(fruit_name)
new_good.append(price)
# print(new_good)
goods.append(new_good)
print('Новый ассортимент:', goods)
count = len(goods)
# print(count)
# for i in range(1, count+1):
#     goods[i-1][1] = round(int(goods[i-1][1]) * 1.08, 2)
    # print(goods[i-1][1])
for y in goods:
    y[1] = round(int(y[1]) * 1.08, 2)

print("Новый ассортимент с увел. ценой:", goods)