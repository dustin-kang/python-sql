```
1. 프로그래밍 기본 문법 공부(파이썬)
2. 알고리즘 기본100제(코드업:기초100제)
3. 백준 문제풀기(그리디, 탐색, 기초 동적프로그래밍 50문제씩)
4. 기출문제 풀기(프로그래머스:카카오)
코드포스 블루레벨 정도면 코딩테스트 합격 가능(또는 삼성 역량 테스트 B형)
```

### 📂 [pythons/baekjoon](https://github.com/dustin-kang/python-sql/tree/main/pythons/baekjoon)
파이썬 백준 문제 풀이

### 📂 [pythons/leetcode](https://github.com/dustin-kang/python-sql/tree/main/pythons/leetcode)
파이썬 리트코드 문제 풀이

### 📂 [pythons/data_structure](https://github.com/dustin-kang/python-sql/tree/main/pythons/data_structure)
파이썬 자료구조 문제 풀이


## Code Snippet
- 타입 힌트 오류 확인 코드
```
$ pip install mypy
$ mypy solution.py
```
- 메모리 점유율 확인
```python
import sys
sys.getsizeof(a)
```
- 파이썬 시간 모듈
```python
import time

start_time = time.time() # 측정 시작

# ~~~~~~~~~ 프로그램 타임 코드 ~~~~~~~~~~

end_time = time.time() # 측정 끝

print("소요시간 : ", end_time - start_time) # 수행시간 출력
```

- 데코레이팅을 이용한 시간 모듈
```py
import time

def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn

@logging_time
def my_func1():
    print("Hello world")

# No decorator
def my_func2():
    print("Good bye")

@logging_time
def my_func3():
    print("I wanna go home")

if __name__=="__main__":
    my_func1()
    my_func2()
    my_func3()
```