data_strings = [ "RU:Electronics:1500", "RU:Clothing:800", "KZ:Electronics:1200", "RU:Electronics:500" ]
from collections import defaultdict
# Двухуровневый defaultdict для автоматического создания вложенности
result = defaultdict(lambda: defaultdict(int))
for item in data_strings:
    region, category, sales = item.split(":") # Автоматически создаст ключи и сложит значения при повторе
    result[region][category] += int(sales) # Преобразуем в обычный словарь
final_result = {k: dict(v) for k, v in result.items()}
print(final_result)