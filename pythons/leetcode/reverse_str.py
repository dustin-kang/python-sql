"""
<문자열 뒤집기>

"""
# 1. 반복문 조건문 을 대입한 예
def reverse_str(strlist):
    left, right = 0, len(strlist)-1 
    while left < right: # 인덱스가 넘어가면 종료
        strlist[left], strlist[right] = strlist[right], strlist[left]
        left += 1
        right -= 1
        
    return strlist

strlist = ['a', 'b', 'c', 'd']
print(reverse_str(strlist)) # 뒤집기 후
print(strlist) # 뒤집기 전

# 2. 리스트 메소드를 사용한 예 (reverse)
strtest2 =['a','b','c','d']
strtest2.reverse()
print(strtest2)

# 3. 파이썬 내장함수
strtest3 =['a','b','c','d']
tuple_test =('a','b','c','d')

print(strtest3) 
print(list(reversed(strtest3)))
print(tuple(reversed(strtest3)))
print(strtest3)