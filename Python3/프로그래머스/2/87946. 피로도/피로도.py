def solution(k, dungeons):
    n = len(dungeons)                 # 던전 개수
    visited = [False] * n             # i번 던전을 이미 갔는지 체크
    best = 0                          # 최대 탐험 개수 저장

    def dfs(fatigue, count):
        nonlocal best                 # 바깥(best) 변수를 내부에서 갱신하겠다
        best = max(best, count)       # 현재까지 깬 개수로 최댓값 갱신

        for i in range(n):            # 다음에 갈 던전을 하나 고르는 선택
            need, cost = dungeons[i]  # 최소 필요 피로도, 소모 피로도
            if not visited[i] and fatigue >= need:  # 아직 안 갔고, 들어갈 수 있으면
                visited[i] = True                 # 1) 방문 처리(선택)
                dfs(fatigue - cost, count + 1)    # 2) 다음 상태로 재귀(탐색)
                visited[i] = False                # 3) 방문 해제(되돌리기=백트래킹)

    dfs(k, 0)                          # 시작: 피로도 k, 깬 던전 0개
    return best                        # 최댓값 반환

