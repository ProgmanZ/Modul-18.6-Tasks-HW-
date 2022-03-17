# a = 'utifulBea si terbet ntha y/ugl icitExpl is erbett than icit/impl eSimpl si rbette hant ex/compl'
a = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm ' \
            'tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ' \
            'ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft ' \
            '(ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
            'Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg ' \
            'hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf ' \
            'zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ' \
            'ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs ' \
            'boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
            'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO ' \
            'bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip"'

user_text = a.split()
new_word = ''
new_line_text = []
new_user_text = ''
k = 3

for word in user_text:
    if len(word) == 2 and k % 2 == 1:
        new_word = word[-1:] + word[:-1]
    else:
        new_word = word[-k:] + word[:-k]

    new_line_text.append(new_word)

    if '/' in word:
        k += 1
        new_line_text.append('\n')

new_user_text = ' '.join(new_line_text)


print(new_user_text)