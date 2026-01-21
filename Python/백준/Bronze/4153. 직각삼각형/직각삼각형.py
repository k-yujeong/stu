# 직각삼각형

result=[]

while True:
    nums = [*map(int,input().split())]
    if nums[0]==nums[1]==nums[2]==0:
        break

    nums = sorted(nums)

    if (nums[0]*nums[0])+(nums[1]*nums[1]) == (nums[2]*nums[2]):
        result.append("right")
    else:
        result.append("wrong")


print(*result,sep='\n')