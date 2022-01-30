user_text = 'utifulBea si terbet ntha y/ugl'
user_text = user_text.split(' ')
print(user_text)
new_text = []
for i in user_text:
    new_text.append(i[-3:] + i[:-3])

print(new_text)
