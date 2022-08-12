cro_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
result = ''
cnt = 0

for char in cro_word:
    if char in word:
        result += char
        cnt += 1

cnt += len(word) - len(result)

print(cnt)