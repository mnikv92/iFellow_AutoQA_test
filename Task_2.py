def fst_rep_char(word):

    # set выбран по причине наиболее быстрой проверки принадлежности
    # данных множеству, что будет критично для больших объемов данных
    checked_chars = set()
    for c in word:
        if c in checked_chars:
            return c
        checked_chars.add(c)

    return None


word = 'Hello'
result = fst_rep_char(word)
print('Повторяющийся символ - ' + result)