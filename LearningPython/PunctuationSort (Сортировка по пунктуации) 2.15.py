text_sms = []
one_text = input('Первое сообщение: ')
two_text = input('Второе сообщение: ')

if one_text.count('!') > two_text.count('?'):
    text_sms.append(one_text)
    text_sms.append(two_text)

elif one_text.count('!') < two_text.count('?'):
    text_sms.append(two_text)
    text_sms.append(one_text)

else:
    text_sms.append('Ой')
print(text_sms)
