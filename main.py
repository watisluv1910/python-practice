def spell(text):
    res = []
    d = get_dict()

    for word in text.split():
        repl_word, repl_dist, repl_popular = word, 3, 0

        for sample_word in d.keys():
            table, dist = damerau_levenshtein(word, sample_word)
            if dist < 3 and (dist < repl_dist or (dist == repl_dist and d[sample_word] > repl_popular)):
                repl_word, repl_dist = sample_word, dist
                repl_popular = d[sample_word]

        res.append(repl_word)

    return " ".join(res)


def get_dict():
    d = {}
    with open("./res/words.txt", encoding="utf-8") as f:
        for line in f:
            (key, val) = line.split()
            d[key] = int(val)
    return d


def equals(letter_1, letter_2):
    sim_r = 'АаВСсЕеКМОоРрТХху'
    sim_e = 'AaBCcEeKMOoPpTXxy'

    if letter_1 == letter_2:
        return True
    elif letter_1 in sim_r and letter_2 in sim_e \
            and sim_r.index(letter_1) == sim_e.index(letter_2):
        return True
    elif letter_2 in sim_r and letter_1 in sim_e \
            and sim_r.index(letter_2) == sim_e.index(letter_1):
        return True

    return False


def damerau_levenshtein(str_1, str_2):
    add_cost, del_cost = 1, 1
    cols, rows = len(str_1), len(str_2)

    if cols > rows:
        str_1, str_2 = str_2, str_1
        cols, rows = rows, cols

    table = [[0] * (cols + 1)] * (rows + 1)
    table[0] = list(range(cols + 1))

    current_row = table[0]
    for i in range(1, rows + 1):
        previous_row, current_row = current_row, [i] + [0] * cols
        for j in range(1, cols + 1):
            add, delete, change = \
                previous_row[j] + add_cost, \
                current_row[j - 1] + del_cost, previous_row[j - 1]

            if i > 1 and j > 1 and equals(str_1[j - 1], str_2[i - 2]) and equals(str_1[j - 2], str_2[i - 1]):
                pass
            elif not (equals(str_1[j - 1], str_2[i - 1])):
                change += 1

            current_row[j] = min(add, delete, change)
        table[i] = current_row

    return table, table[rows][cols]


if __name__ == "__main__":
    print(damerau_levenshtein('Иванов Ивн Ивнаович', 'Ивaнов Иван Иванович')[1])
    print(spell('Иванов Ивн Ивнаович'))
