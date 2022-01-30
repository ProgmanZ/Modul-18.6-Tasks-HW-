# Задача 9. Сообщение

user_text = list(input("Сообщение: "))
new_user_text = []
temp_word = []
for i in user_text:
    if i.isalpha():
        temp_word.append(i)
    else:
        new_user_text.extend(list(reversed(temp_word)))
        new_user_text.extend(i)
        temp_word = []
new_user_text = ''.join(new_user_text)
print("Новое сообщение: ", new_user_text)
