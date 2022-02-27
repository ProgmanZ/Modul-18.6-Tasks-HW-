user_text = 'utifulBea si terbet ntha y/ugl icitExpl is erbett than icit/impl eSimpl si rbette hant ex/compl ' \
            'xComple is better anth cated/compli tFla si etterb ntha nested/ arseSp is tterbe than nse/de ' \
            'tyReadabili unts/co cialSpe cases (taren cialspe ghenou to break '
user_text = user_text.split(' ')
print(user_text)
new_text = []
len_letter = 0
temp_letter = []
text = ''
k = 0

for letter in user_text:
    if not k % 2 and len(letter) == 2:
        temp_letter = letter[-1:] + letter[:-1]
        new_text.append(temp_letter)
        continue

    # temp_letter = letter[-k-3:] + letter[:-k-3]
    temp_letter = letter[(len(letter) + -1 * k) % len(letter):] + letter[:(len(letter) + -1 * k) % len(letter)]

    if str(temp_letter).endswith('/'):
        new_text.append(temp_letter[:-1] + '\n')
        k += 1
        continue

    new_text.append(temp_letter)

    temp_letter = []
text = ' '.join(new_text)

print(text)
