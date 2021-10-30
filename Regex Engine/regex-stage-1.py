def reg_math(in_str):
    regular, text = [_ for _ in in_str.split('|')]
    if regular == text:
        return 'True'
    elif regular == '.' or len(regular) == 0:
        return 'True'
    else:
        return 'False'


in_data = input()

print(reg_math(in_data))
