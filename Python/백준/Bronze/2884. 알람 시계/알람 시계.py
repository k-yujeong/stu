# 알람 시계
a, b = map(int,input().split())

time_ = ((a*60)+b)-45
a= (time_//60)%24
b = time_%60


print(a, b)
