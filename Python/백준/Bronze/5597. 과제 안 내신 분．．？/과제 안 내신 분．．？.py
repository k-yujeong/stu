# 과제 안 내신 분 ...?
stu_list = [int(input()) for i in range(28)]

stu_list.sort()

miss_stu = []


for i in range(1, 31):
    if (i) not in stu_list:
       miss_stu.append(i)





print(*miss_stu, sep='\n')