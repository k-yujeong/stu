# 부녀회장이 될테야

Test_case = int(input())
result = []


for i in range(Test_case):
    k =int(input())
    n = int(input())
    de_flr = [i for i in range(1,n+1)]  # 0층, 1호~n호

    # k층
    for _ in range(k):
        for i in range(1,n):
            de_flr[i]+=de_flr[i-1]


# 출력값 = Test_case 별, K층의 N호수의 거주민 수
    result.append(de_flr[n-1])

print(*result,sep='\n')