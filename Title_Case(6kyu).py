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

def test(title, minor_words, expect):
    answer = title_case(title) if minor_words is None else title_case(title, minor_words)
    if answer == expect:
        result = 'AC! '
    else:
        result = 'Error! '

    message = "Gave title={0}{1}. Expected {2} but got {3}.".format(
        repr(title),
        '' if minor_words is None else ', minor_words=' + repr(minor_words),
        repr(expect),
        repr(answer))
    print(result + message)
    # Test.expect(answer == expect, message)


if __name__ == '__main__':
    test('', '', '')
    test('aBC deF Ghi', None, 'Abc Def Ghi')
    test('ab', 'ab', 'Ab')
    test('a bc', 'bc', 'A bc')
    test('a bc', 'BC', 'A bc')
    test('First a of in', 'an often into', 'First A Of In')
    test('a clash of KINGS', 'a an the OF', 'A Clash of Kings')
    test('the QUICK bRoWn fOX', 'xyz fox quick the', 'The quick Brown fox')
