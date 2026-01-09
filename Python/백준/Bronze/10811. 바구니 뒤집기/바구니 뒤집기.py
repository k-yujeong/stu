# 바구니 뒤집기
n, m = map(int, input().split())


# 바구니 생성
bas_k = list(range(1,n+1))


# 역순 만들기
for i in range(m):
    i, j = map(int, input().split())
    bas_k[i-1:j] = bas_k[i-1:j][::-1]


print(*bas_k)