data = input()
chars = data[len(data) - 1:]
str = data[:len(data) - 3]
count = 0

for i in str:
    if i == chars:
        count += 1
    else:
        break

print(count)
