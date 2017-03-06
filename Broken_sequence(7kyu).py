def find_missing_number(sequence):
    # your code here
    sequence_list = sequence.split()
    if len(sequence_list) > 0:
        for x in sequence_list:
            if not x.isdigit():
                return 1
        num_list = [int(i) for i in sequence_list]
        num_list.sort()
        t = 1
        for x in num_list:
            if int(x) == t:
                t += 1
                continue
            else:
                return t
        return 0
    else:
        return 0
