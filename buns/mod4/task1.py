def chars(chars):
    if len(set(chars)) == len(chars):
        return "Все числа разные"
    if chars.count(chars[0]) == len(chars):
        return "Все числа равны"
    return "Есть равные и неравные числа"


print(chars([5, 60, 10]))
