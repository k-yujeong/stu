# 최댓값과 최솟값
def solution(s):
    s_=list(map(int,s.split()))
    answer = str(min(s_))+' '+str(max(s_))
    return answer