# stack
def solution(arr):
    answer = []
    for num in arr:
        if not answer:
            answer.append(num)
        elif answer[-1] != num:
            answer.append(num)
        
    return answer

# index
def solution(arr):
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            res.append(arr[i])
    return res