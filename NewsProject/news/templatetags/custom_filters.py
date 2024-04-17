from django import template


register = template.Library()

CURRENCIES_SYMBOLS = {'ellipsis': '...', 'exclamation_mark': '!'}


@register.filter()
def punctuation_marks(value, mark='ellipsis'):
    postfix = CURRENCIES_SYMBOLS[mark]
    return f'{value}{postfix}'


# ПРЕДПОЛОЖИМ, ЧТО НЕЦЕНЗУРНЫЕ СЛОВА НАЧИНАЮТСЯ С ГЛАСНОЙ ЗАГЛАВНОЙ БУКВЫ
@register.filter()
def censor(value):
    text = value.split()
    new_text = []

    for i in range(len(text)):
        word = text[i]
        first_symbol = word[0]
        if first_symbol in 'АИЕЁОУЫЭЮЯ':
            new_word = first_symbol
            if len(word) == 1:
                new_word = '*'
                new_text.append(new_word)
            else:
                for x in range(len(word)):
                    if x != 0:
                        if word[x].isalnum():
                            new_word += '*'
                        else:
                            new_word += word[x]
                new_text.append(new_word)
        else:
            new_text.append(word)

    new_text = ' '.join(new_text)

    return new_text


# @register.filter()
# def date_time_creation_comment(value):
#     return f'когда был написан комментарий: {value}'
