enter_string = input('Введите строку: ')
enter_symbol = input('Введите дополнительный символ: ')

list_doubled = [x * 2 for x in enter_string]
list_with_symbol = [x + enter_symbol for x in list_doubled]

print('Список удвоенных символов:', list_doubled)
print('Склейка с дополнительным символом:', list_with_symbol)