def solution(s, n):
    res=[]
    for ch in s:
        if ch == " ":
            res.append(ch)
        elif 'A' <= ch <= 'Z':  # 대문자 
            base = ord('A')
            res.append(chr((ord(ch)-base+n)%26+base))   # 아스키 코드값 변환
        else:           # 'a' <= ch <= 'z':
            base = ord('a')
            res.append(chr((ord(ch)-base+n)%26+base))
    return ''.join(res)           

# index ver.
import string

def solution(s, n):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    
    res = []
    for ch in s:
        if ch == ' ':
            res.append(' ')
        elif ch.isupper():  # 대문자
            idx = upper.index(ch)          # 여기서 "찾기"
            res.append(upper[(idx+n) % 26]) # 0~25이므로 원형 구조 -> 26
        else:
            idx = lower.index(ch)
            res.append(lower[(idx+n) % 26])
    return ''.join(res)
