# 상수
num = list(map(str, input().split()))

if num[0][::-1] > num[1][::-1]:
    print(num[0][::-1])

else:
    print(num[1][::-1])
