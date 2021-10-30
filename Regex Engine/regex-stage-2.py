def reg_math(in_str):
    regular, text = [_ for _ in in_str.split('|')]
    if regular == text:
        return True
    elif regular == '.' or len(regular) == 0:
        return True
    else:
        return False


def match_eq_len_str(in_str):
    regular, text = [_ for _ in in_str.split('|')]
    if len(regular) > 0 and len(text) == 0:
        return 'False'
    for r, t in zip(regular, text):
        # print(r + '|' + t)
        if reg_math(r + '|' + t):
            continue
        else:
            return 'False'
    return 'True'


in_data = input()

print(match_eq_len_str(in_data))
