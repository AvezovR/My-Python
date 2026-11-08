small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}
big_storage.update(small_storage)

while True:
    product_name = input('Какой товар ищете?: ').lower()
    if product_name in big_storage:
        print(product_name, 'осталось', big_storage.get(product_name), 'шт.')
        continue
    else:
        print('Таково товара нет')
        continue