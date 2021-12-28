# Задача 3. Файлы

file_name = input('Название файла: ')  # @example.txt

file_extension = ['.txt', '.docx']
symbol_error = '@№$%^&*()'

if True in [file_name.startswith(i) for i in list(symbol_error)]:
    print('Ошибка: название начинается на один из специальных символов.')
elif not(True in [file_name.endswith(i) for i in file_extension]):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
