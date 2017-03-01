def title_case(title, minor_words = ''):
    new_list = []
    new_string = ''
    title_l = title.split()
    minor_words_l = minor_words.split()
    minor_words_l_lower = [x.lower() for x in minor_words_l]

    title_l_num = len(title_l)
    minor_words_l_num = len(minor_words_l)

    # first word upper()
    if title_l_num > 0:
        new_list.append(initial_upper(title_l[0]))
        if title_l_num > 1 and minor_words_l_num > 0:
            for t in range(1, title_l_num):
                if  title_l[t].lower() in minor_words_l_lower:
                    new_list.append(title_l[t].lower())

                else: 
                    new_list.append(initial_upper(title_l[t]))

            new_string = ' '.join(new_list)
            return new_string

        else:
            for t in range(1, title_l_num):
                new_list.append(initial_upper(title_l[t]))

            new_string = ' '.join(new_list)
            return new_string

    else:
        return new_string

def initial_upper(word): 
    new_word = ''
    if len(word) > 0:
        new_word = word[0].upper()
    if len(word) > 1:
        for t in range(1, len(word)):
            new_word = new_word + word[t].lower()
    return new_word
