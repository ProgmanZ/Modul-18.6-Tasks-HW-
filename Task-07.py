# Задача 7. IP-адрес 2


flag = True

def check_digit(list_digit):
    list_temp = [True if i.isdigit() else False for i in list_digit]
    return False in list_temp

def search_nodigit(list_check):
    tmp_list = [i for i in list_check if not i.isdigit()]
    return  tmp_list

while flag:

    ip_address = input('Введите IP: ').split('.')
    if len(ip_address) != 4:
        print('IP адрес - это четыре группы положительных чисел, разделённые точками')

    elif check_digit(ip_address):
        print(','.join(search_nodigit(ip_address)), ' - Проверьте введенные вами данные.\n'
                                                    'IP адрес - это четыре группы положительных чисел,'
                                                    ' разделённые точками')

    elif 0 == int(ip_address[0]) or 0 == int(ip_address[3]):
        print('IP адрес не может начинаться и заканчиваться значением = 0')

    else:
        for i in ip_address:
            if int(i) >= 255:
                flag = True
                print(i, 'Значение превышает или равно 255')
            else:
                flag = False

print('\nIP-адрес корректен: ', '.'.join(ip_address))
