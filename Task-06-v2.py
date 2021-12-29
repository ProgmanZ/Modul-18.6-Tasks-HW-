# Задача 6. Сжатие v2.

user_string = input('Введите строку: ')
size_list = len(user_string)
result_list = user_string[0]
count = 0

for i in range(size_list):
    tmp_list = user_string[i:]
    if result_list[-1] != tmp_list[0]:
        result_list += str(count) + user_string[i]
        count = 1
    else:
        count += 1
result_list += str(count)

print(result_list)
