# Задача 6. Сжатие

# Введите строку: aaAAbbсaaaA
# Закодированная строка: a2A2b2с1a3A1

user_string = input('Введите строку: ')
count = 1
len_word = len(user_string)
# result = user_string[0]
result = user_string[0]
ind = 0
for i in range(0, len_word):
    if user_string[i] == result[ind]:
        count += 1
    else:
        result += str(count)
        result += user_string[i-1]
        count = 0
        ind += 1

print(result)