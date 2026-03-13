def solution(tickets):
    graph = {}
    for t in tickets:
        a = t[0]
        b = t[1]
        if a not in graph:  # 출발지 값이 key 값으로 없다면
            graph[a] = []
        graph[a].append(b)  # 항상 append 되어야 함
    for a in graph:
        graph[a].sort(reverse=True) # 알파벳 역순서
    # 시작은 항상 "ICN"
    stack = ["ICN"]
    answer = []

    while stack:
        cur = stack[-1] # 현재 위치
        if cur in graph and graph[cur]:
            next = graph[cur].pop() # 알파벳 순서가 앞서는 경로부터 pop
            stack.append(next)
        else:
            answer.append(stack.pop())

    # route 뒤집어서 반환 (막힌 지점으로부터 쌓임)
    return answer[::-1]