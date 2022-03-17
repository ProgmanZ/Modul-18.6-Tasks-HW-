# Задача 8. Бегущая строка

def check_string(one_string, two_string):
    i = 1
    while i <= len(one_string):
        cc_first = one_string[i:] + one_string[:i]
        if two_string == cc_first:
            return True, i
        i += 1
    return False, i


first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')
len_first = len(first_string)
count = 0
while len_first:
    if first_string[count] == second_string[-1 * len_first]:
        count += 1
    else:
        len_first -=1
if len(first_string) == len(second_string):

    flag, result = check_string(first_string, second_string)

    print("Первая строка получается из второй со сдвигом {}.".format(result) if flag
          else "Первую строку нельзя получить из второй с помощью циклического сдвига.")
else:

    print("Первую строку нельзя получить из второй с помощью циклического сдвига т.к. длинна строк имеет разное "
          "значение.")
