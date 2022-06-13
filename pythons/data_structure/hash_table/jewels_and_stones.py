"""
[771]
보석과 돌
- 문제 : J는 보석이며 S는 갖고 있는 돌이다.
 S에는 보석이 몇 개나 있을까? 
 대소문자는 구분한다.


- 난이도 : ⭐️
- 시간복잡도 : 


[EXAMPLE 1]
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

[EXAMPLE 2]
Input: jewels = "z", stones = "ZZ"
Output: 0

"""
import collections

class Solution:
    def numJewlsInStones(self, jewels: str, stones : str) -> int:
        """
        해시테이블을 이용한 풀이 방법
        """
        count = 0
        freqs = {}
        
        for char in stones:
            if char not in freqs: # 글자가 freqs 딕셔너리에 존재하지 않은 경우
                freqs[char] = 1
            else :  # 이전에 존재했던 경우
                freqs[char] += 1

        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count
    
    def numJewlsInStones2(self, jewels: str, stones : str) -> int:
        """
        `defaultdict`을 이용한 풀이 방법
        - 디폴트 딕셔너리가 있기 때문에 if 조건을 굳이 만들어 판별할 필요 없어짐.
        """
        count = 0
        freqs = collections.defaultdict(int)
    
        
        for char in stones:
                freqs[char] += 1

        for char in jewels:
                count += freqs[char]

        return count

    def numJewlsInStones3(self, jewels: str, stones : str) -> int:
        """
        `Counter`을 이용한 풀이 방법 (Counter 계산 생략)
        - 디폴트 딕셔너리가 있기 때문에 if 조건을 굳이 만들어 판별할 필요 없어짐.
        """
        count = 0
        freqs = collections.Counter(stones) # 돌(stones)의 빈도수를 계산
    
        for char in jewels:
                count += freqs[char]

        return count

    def numJewlsInStones4(self, jewels: str, stones : str) -> int:
        """
        파이썬 다운 방식
        - `[s for s in stones] : ['a', 'A', 'A', 'b', 'b', 'b','b']`
        - `[s in jewels for s in stones] : [T, T, T, F, F, F, F]`
        """

        return sum(s in jewels for s in stones)

J1,S1 = "aA", "aAAbbbb"
J2,S2 = "z", "ZZ"

solution = Solution()
solution.numJewlsInStones3(J1, S1)

