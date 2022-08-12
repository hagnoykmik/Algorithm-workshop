cro_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for char in cro_word:
    if char in word:
        word = word.replace(char, '.')
        cnt = len(word)
print(cnt)