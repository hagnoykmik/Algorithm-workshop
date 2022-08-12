word = input()
result = ''

for char in word: #제거 대상인 단어를
    if char not in 'CAMBRIDGE': #캠브릿지의 철자와 비교하여 겹치지않으면
        result += char #빈문자열에 추가한다

print(result)