x = int(input())

# dp[i] = i를 1로 만드는 최소 연산 횟수
dp = [0] * (x + 1)

# 1은 이미 1이므로 0번
dp[1] = 0

for i in range(2, x + 1):
    # 1을 빼는 경우를 기본값으로 둔다
    dp[i] = dp[i-1] + 1 

    # 2로 나누어 떨어지면 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) 

    # 3으로 나누어 떨어지면 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) 

print(dp[x])