def solution(n):
    answer = 0
    for i in range(2,n+1):  # 2도 가능함
        if n%i==1:
            answer = i
            break
            
    return answer