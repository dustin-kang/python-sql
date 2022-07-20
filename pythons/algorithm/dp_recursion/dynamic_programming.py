"""
11726
2XN 타일링

2 X 1 의 경우의 수는 1개
2 X 2 의 경우의 수는 2개
2 X 3 의 경우의 수는 3개 = 2 + 1
2 X 4 의 경우의 수는 5개  = 3 + 2

[!] 점화식 패턴 찾아내기
n-1 + A
n-2 + B

"""

# num = int(input())

def twoxn(num):
    cache = [0] * 1001
    cache[1] = 1
    cache[2] = 2
    
    for index in range(3, 1001):
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[num] % 10007

#print(twoxn(num))

"""
파도반 수열

"""

T = int(input())
cache = [0] * 101
cache[1] = 1
cache[2] = 1
cache[3] = 1
first = 4

for count in range(1,T+1):
    num = int(input())
    if cache[num] == 0:
        for index in range(first, 101):
            cache[index] = cache[index-2] + cache[index-3]
            first += 1
            if num == index :
                print(cache[num])
                break
    else :
        print(cache[num])
    