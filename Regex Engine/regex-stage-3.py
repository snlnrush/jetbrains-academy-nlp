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
        return False
    for r, t in zip(regular, text):
        # print(r + '|' + t)
        if reg_math(r + '|' + t):
            continue
        else:
            return False
    return True


def match_diff_len_str(in_str):
    if match_eq_len_str(in_str):
        return True
    regular, text = [_ for _ in in_str.split('|')]
    for idx in range(len(text)):
        if match_eq_len_str(regular + '|' + text[idx: len(regular) + idx]):
            return True
        else:
            continue
    return False


in_data = input()


print(match_diff_len_str(in_data))
