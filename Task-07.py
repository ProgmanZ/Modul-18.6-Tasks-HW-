# Задача 7. IP-адрес 2

def digit_check(ip_list):
    return False if False in [True if x.isdigit() else False for x in user_string] else True


def size_check(ip_list):
    return sum([int(x) if int(x) > 255 else 0 for x in user_string])


while True:
    user_string = input('Введите IP адрес: ').split('.')

    if len(user_string) != 4:
        print('IP адрес представляет 4 группы цифр, разделенных точкой.')

    else:
        if not digit_check(user_string):
            print('В IP адресе должны использоваться только цифры из диаппазона от 0 до 255.')
            continue

        elif 0 == int(user_string[0]) or 0 == int(user_string[3]):
            print('Первая или последняя группа цифр не может быть = 0.')
            continue

        elif size_check(user_string) > 0:
            print('В IP адресе должны использоваться только цифры из диаппазона от 0 до 255.')
            print(size_check(user_string), 'превышает 255.')
            continue

        else:
            print('IP адрес верный.')
            break
