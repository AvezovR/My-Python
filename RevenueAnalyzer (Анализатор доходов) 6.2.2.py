incomes = {'apple': 5600.20,'orange': 3500.45,'banana': 5000.00,
           'bergamot': 3700.56,'durian': 5987.23,'grapefruit': 300.40,
           'peach': 10000.50,'pear': 1020.00,'persimmon': 310.00,
}

total_income = sum(incomes.values())
print('Общий доход за год составил', total_income, 'рублей')

min_income = min(incomes.values())
product = [key for key, value in incomes.items() if value == min_income]
print(f"Cамый маленький доход у {''.join(product)}. Он составляет {min_income} рублей")

incomes.pop(''.join(product))
print(f"Итоговый словарь: {incomes}")
