# Задача 4. Заглавные буквы

user_string = input('Введите строку: ').split()

user_string = ' '.join([word.capitalize() for word in user_string])

print('Результат: ',user_string)
