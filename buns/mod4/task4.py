def palindrome(word):
    firtsChars = {}
    for char in word:
        if char in firtsChars:
            firtsChars[char] += 1
        else:
            firtsChars[char] = 1

    secondChars = 0
    chars = ''
    palindromes = ''

    for char in firtsChars:
        if firtsChars[char] % 2 != 0:
            secondChars += 1
            if secondChars > 1:
                return "Невозможно сформировать палиндром из данного слова."
            else:
                chars = char

        for _ in range(firtsChars[char] // 2):
            palindromes += char

    return palindromes + chars + palindromes[::-1]


print(palindrome("мистеррестиммими"))
