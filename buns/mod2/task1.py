numbers = input()
num1, num2, counter = 0, 0, 0

for char in numbers:
    if char == ',':
        num1 = int(numbers[:counter])
        num2 = int(numbers[counter + 2:])
    counter += 1
print(num1 % num2)
