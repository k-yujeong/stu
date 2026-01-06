# 윤년
x=int(input())

def yeer(x):
    if x%4 ==0:
        if x%100 !=0 or x%400 ==0:
            return 1

        else:
            return 0
        

    else:
        return 0

print(yeer(x))