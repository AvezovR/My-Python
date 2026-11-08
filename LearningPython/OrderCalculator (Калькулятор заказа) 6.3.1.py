order = {'apple': 2,'banana': 3,'pear': 1,
         'watermelon': 10,'chocolate': 5}
incomes = {'apple': 5600.20,'orange': 3500.45,'banana': 5000.00,'bergamot': 3700.56,
    'durian': 5987.23,'grapefruit': 300.40,'peach': 10000.50,'pear': 1020.00,
    'persimmon': 310.00}
sum_incomes = 0
for i_product in incomes:
    if i_product in order:
        print(f'{i_product}: {incomes.get(i_product,'0')}')
        i_income = float(incomes.get(i_product, '0'))
        i_count = float(order.get(i_product, '0'))
        sum_incomes += i_income * i_count
    else:
        print(f'{i_product}: {order.get(i_product,'0')}')

print(f'Суммарная стоимость - {sum_incomes}')

