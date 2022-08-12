#교수님

cro_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

#크로아티아 알파벳을 . 으로 바꾸면 1자리 문자가 되지 않을까?
for change in cro_word:
    word = word.replace(change,'.') #immutable이니까 word에 새롭게 할당해줘야함

print(len(word))
