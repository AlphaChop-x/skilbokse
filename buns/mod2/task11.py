line = input()
numbers = ""
bol = False

for i_symb in line:
    if i_symb != " ":
        numbers += i_symb
        print(numbers)

counter = 1

for first_num in numbers:
    for second_num in numbers[counter:]:
        if first_num == second_num:
            bol = True
        else:
            continue
    counter += 1

print(bol)
