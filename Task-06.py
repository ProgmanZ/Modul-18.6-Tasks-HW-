# Задача 6. Сжатие

user_string = input('Введите строку: ')
count = 1
len_word = len(user_string)
result = user_string[0]
ind = 0

for i in range(1, len_word):
    if user_string[i] == result[ind]:
        count += 1
    else:
        result += str(count)
        result += user_string[i]
        count = 1
        ind += 2
result += str(count)

print(result)
