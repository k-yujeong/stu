def solution(number, k):
    stack = []
    for digit in number:
        while stack and k>0 and stack[-1] < digit:  # stack == True, 
            stack.pop()
            k-=1    # 제거 숫자 낮춤
        stack.append(digit)    # 큰 수 삽입
    if k>0:
        stack = stack[:-k]    # 더 이상 키울 수 없으므로 끝에 슬라이싱
            
            
    return "".join(stack)
