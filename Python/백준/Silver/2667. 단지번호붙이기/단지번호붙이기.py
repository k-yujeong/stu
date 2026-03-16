N = int(input())
home = []

for _ in range(N):
    num = list(input())
    home.append(num)

# 상하좌우 이동용, 배열은 [행][열]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 1. 현재 집 방문 처리
    home[x][y] = '0'

    # 2. 현재 집 하나 포함
    count = 1

    # 3. 상하좌우 확인
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 4. 범위 안인지 확인
        if 0 <= nx < N and 0 <= ny < N:
            # 5. 다음 칸이 집이면 계속 탐색
            if home[nx][ny] == '1':
                count += dfs(nx, ny)

    # 6. 이 단지의 집 수 반환
    return count

result = []

# 7. 전체 지도 순회
for i in range(N):
    for j in range(N):
        # 8. 집을 만나면 새로운 단지 시작
        if home[i][j] == '1':
            house_count = dfs(i, j)
            result.append(house_count)

# 9. 오름차순 정렬
result.sort()

# 10. 출력
print(len(result))
for r in result:
    print(r)