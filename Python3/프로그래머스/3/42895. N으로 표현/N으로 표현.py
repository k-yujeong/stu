def solution(N, number):
    # 1. 예외 처리
    if number == N:
        return 1

    # 2. dp 준비
    # dp[i] = N을 i번 사용해서 만들 수 있는 수들의 집합
    dp = [set() for _ in range(9)]

    # 3. 1개 ~ 8개까지 확인
    for i in range(1, 9):
        # 4. 이어붙인 수 넣기(NN)
        dp[i].add(int(str(N) * i))

        # 5. j개 + (i-j)개 조합
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    
                    # N-N에서 0 발생 가능
                    if b != 0:
                        dp[i].add(a//b)

        # 6. 현재 단계에서 number를 만들 수 있으면 종료
        if number in dp[i]:
            return i

    # 7. 8개까지 못 만들면
    # 최솟값이 8보다 크면 -1을 return 합니다.
    return -1