text = '     aaa(hello)bbbb   '

mystr = text.strip()       # strip 메소드는 문자열의 공백을 채워서 반환
print(mystr)
apos = mystr.find('(')  # (의 위치
dpos = mystr.find(')')  # )의 위치

print('apos : ', apos)
print('dpos : ', dpos)

if apos > -1 and dpos > -1 and dpos > apos+1:
    print(mystr[apos+1:dpos])