goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

def plural(number, one, two, many):
    if 11 <= (number % 100) <= 14:
        return many
    last_digit = number % 10
    if last_digit == 1:
        return one
    elif 2 <= last_digit <= 4:
        return two
    else: return many

for product_name in goods:
    for product_code in goods.values():
        i_quantity = 0
        i_price = 0
        if product_code == goods[product_name]:
            for len_store in range (len(store[product_code])):
                i_quantity += store[product_code][len_store]["quantity"]
                i_price += store[product_code][len_store]["price"] * store[product_code][len_store]["quantity"]
            print(f'{product_name} - {i_quantity} {plural(i_quantity, 'штука', 'штуки', 'штук')}, стоимость {i_price:d} рублей')