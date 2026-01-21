# 좌표 정렬하기 , 내 코드
N = int(input())
result=[]

for _ in range(N):
    nums = [*map(int,input().split())]
    result.append(nums)

result.sort()

for x, y in result:
    print(x, y)