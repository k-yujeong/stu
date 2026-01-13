# 알파벳 찾기
import string
lowercase_letters = list(string.ascii_lowercase)
lowercase_letters

result = []

S = input()

for letter in lowercase_letters:
    if letter in S:
        result.append(S.index(letter))
    else:
        result.append(-1)

print(*result)
