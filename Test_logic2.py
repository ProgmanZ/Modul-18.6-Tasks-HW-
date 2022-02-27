a = 'utifulBea si terbet ntha y/ugl icitExpl is erbett than icit/impl eSimpl si rbette hant ex/compl'
a = a.split()
new_text = ''
k = 6

for i in a:
    # temp_letter = i[(len(i) + k) % len(i):] + i[:(len(i) + k) % len(i)]
    temp_letter = i[k % len(i):] + i[:k % len(i)]
    new_text += str(temp_letter) + ' '
    if '/' in i:
        k -= 2
    if k == -1:
        k = 6

print(new_text)