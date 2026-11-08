product_price = []

for i in range(5):
    print('Цена на товар ', end=':')
    price = float(input())
    product_price.append(price)

first_proceed_price = int(input('Повышение на первый год: '))
second_proceed_price = int(input('Повышение на второй год: '))

first_price = [x * (100 + first_proceed_price) / 100 for x in product_price]
second_price = [x * (100 + second_proceed_price) / 100 for x in first_price]

print('Сумма цен за каждый год:', sum(product_price), round(sum(first_price), 2), round(sum(second_price), 2))