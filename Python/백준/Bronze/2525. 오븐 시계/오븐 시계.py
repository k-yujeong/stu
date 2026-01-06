
# 오븐 시계

a,b = map(int, input().split())
c = int(input())

def oven_timer(a, b, c):
    total = b+c
    a=(a + (total//60))%24
    b=total %60

    return a,b
    

print(*oven_timer(a, b, c))