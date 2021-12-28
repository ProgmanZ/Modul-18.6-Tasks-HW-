# Задача 5. Пароль

while True:
    user_passwd = input('Придумайте пароль: ')

    result_len = True if len(user_passwd) >= 8 else False
    result_upper = True in [i.isupper() for i in user_passwd]
    result_lower = True in [i.islower() for i in user_passwd]
    result_digit = True if sum([1 if i.isdigit() else 0 for i in user_passwd]) >= 3 else False

    if result_len and result_upper and result_lower and result_digit:
        print('Это надёжный пароль!')
        break

    print('Пароль ненадёжный. Попробуйте ещё раз.')
