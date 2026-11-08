from num2words import num2words
from collections import defaultdict

def get_ordinal(number, gender='m'):
    return num2words(number, lang='ru', ordinal=True, to='ordinal', gender=gender).title()

def get_completed_orders(order):
    order_tracking = []
    for i_order in range(1, order + 1):
        i_order_tracking = input(f"{get_ordinal(i_order)} заказ: ")
        order_tracking.append(i_order_tracking)
    return order_tracking

def get_completed_result(entire_order):
    global final_result
    result = defaultdict(lambda: defaultdict(int))
    for i_count in entire_order:
        person, name_pizza, quantity = i_count.split(" ")
        result[person][name_pizza] += int(quantity)
        final_result = {k: dict(v) for k, v in result.items()}
    return final_result

def conclusion(list):
    for i_item in sorted(list.keys()):
        print(i_item, ':')
        for i_name_pizza in sorted(list[i_item].keys()):
            print('     ', i_name_pizza, ':', list[i_item][i_name_pizza])

number_of_orders = int(input('Введите количество заказов: '))
orders = get_completed_orders(number_of_orders)
full_orders = get_completed_result(orders)
print()
conclusion(full_orders)