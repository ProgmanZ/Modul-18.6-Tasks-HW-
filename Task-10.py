# Задача 10. Истина

USER_TEXT = 'vujgvmCfb tj ufscfu ouib z/vhm ' \
            'jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
            'fTjnqm tj scfuuf ibou fy/dpnqm ' \
            'yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
            'uGmb tj fuufsc ouib oftufe/ ' \
            'bstfTq jt uufscf uibo otf/ef ' \
            'uzSfbebcjmj vout/dp ' \
            'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
            'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
            'Fsspst tipvme wfsof qbtt foumz/tjm ' \
            'omfttV mjdjumzfyq odfe/tjmf ' \
            'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
            'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
            'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
            'xOp tj scfuuf ibou /ofwfs ' \
            'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
            'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
            'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
            'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

ENG_DICT = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def dec_stage_second(word_list):
    if '(' in word_list:
        word_list = word_list.replace('(', '\'')
        # word_list = [letter if letter != ')' else '\'' for letter in word]
    return word_list[-(k % len(word_list)):] + word_list[:-(k % len(word_list))]


def dec_stage_one(code, dictionary):
    count = 1
    temp_text = []
    while count:
        for i in code:
            if i in dictionary:
                index_eng = dictionary.index(i) - count
                temp_text.append(dictionary[index_eng])
            else:
                temp_text.append(i)
        count -= 1
    return ''.join(temp_text)


text_from_stage_one = dec_stage_one(USER_TEXT, ENG_DICT).split()
decoded_user_text = []
k = 3

for word in text_from_stage_one:

    new_word = dec_stage_second(word)

    if '/' in new_word:
        new_word = new_word.replace('/', '')
        k += 1
        decoded_user_text.append(new_word)
        decoded_user_text.append('\n')
        continue

    decoded_user_text.append(new_word)

decoded_user_text = ' '.join(decoded_user_text)

print(decoded_user_text)
