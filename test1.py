from numpy import not_equal


t = int(input())
while t>0:
    t-=1
    n = int(input())
    s = input()
    # a, b = [int(x) for x in input().split()]
    # x = list(map(int, input().split()))
    count=1
    for i in range(1, n-1):
        if i!=i-1:
            count+=(i+1)
        else:
            count+=1
    
    print(count)
