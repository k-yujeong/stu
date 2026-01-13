# 행렬 덧셈
A, B = map(int, input().split())
A_m= []
B_m = []
result = [[0 for _ in range(B)] for _ in range(A)] 

for _ in range(A):
    A_row = list(map(int, input().split()))
    A_m.append(A_row)

for _ in range(A):
    B_row = list(map(int, input().split()))
    B_m.append(B_row)

for i in range(A):
    for j in range(B):
        result[i][j] = A_m[i][j] + B_m[i][j]

for num in result:
    print(*num)