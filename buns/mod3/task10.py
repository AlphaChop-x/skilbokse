size = int(input("enter size "))
matrix = [[x for x in range(1, size + 1)] for i in range(size)]

for x in matrix:
    for y in x:
        print(str(y) + ' ', end="")
    print('')

transposed_matrix = [[matrix[j][i] for j in range(size)] for i in range(size)]
print("\n")
for x in transposed_matrix:
    for y in x:
        print(str(y) + ' ', end="")
    print('')
