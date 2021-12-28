# Задача 2. Самое длинное слово

user_string = input('Введите строку: ').split(' ')
long_word = user_string[0]

for i in user_string:
    if len(i) > len(long_word):
        long_word = i
print(long_word)
