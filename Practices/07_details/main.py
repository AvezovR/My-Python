shop = [
        ['каретка', 1200],
        ['шатун', 1000],
        ['седло', 300],
        ['педаль', 100],
        ['седло', 1500],
        ['рама', 12000],
        ['обод', 2000],
        ['шатун', 200],
        ['седло', 2700]
]

# TODO здесь писать код
name_details = input('Название детали: ')
total_details = 0
sum_price = 0

for detail in shop:
        if name_details in detail:
                total_details += 1
                sum_price += int(detail[1])
print('Количество деталей:', total_details )
print('Общая стоимость:', sum_price)
