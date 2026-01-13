import string
lowercase_letters = list(string.ascii_lowercase)

S = input()

for s in lowercase_letters:
    print(S.find(s), end =' ')