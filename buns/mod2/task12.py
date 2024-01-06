phone_number = input()
plus_and_nums = ""
target_symb = "()-" + " "

for i_symb in phone_number:
    if i_symb in target_symb:
        continue
    else:
        plus_and_nums += i_symb

print(plus_and_nums)