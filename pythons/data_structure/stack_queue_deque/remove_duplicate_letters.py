"""
[316]
중복 문자 제거
- 문제 : 중복된 문자를 제외하고 사전식 순서(Lexicographical Order)로 나열하라.
    - "ebcabce"
    - 1. 중복된 문자 제거 : abce (e,b,c 제거)
    - 2. 사전식 순서 : abce

- 난이도 : ⭐️⭐️⭐️
- 시간복잡도: O(n)  (스택풀이가 더 빠르다.)


[EXAMPLE 1]
Input: s = "bcabc"
Output: "abc"

[EXAMPLE 2]
Input: s = "cbacdcbc"
Output: "acdb"
"""

import collections


s1 = "bcabc"
s2 = "cbacdcbc"

class Solution:
    def removeDuplicateLetters_1(self, s : str):
        """
        ### 재귀를 이용한 분리 풀이법
        1. 일치 가능 여부 
            - 접미사 집합(`suffix`)과 전체 집합(`s`)이 일치하는지에 따라 분리 판별
        2. 이미 분리된 문자는 모든 `replace()`로 제거

        - `set()` : 중복이 제거된 요소만 가져올 수 있다.
        """
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 만약 접미사 집합과 전체 집합이 일치하면 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters_1(suffix.replace(char, '')) # 분할 정복을 통해 suffix 감소로 백트래킹
        return ''

    def removeDuplicateLetters_2(self, s: str):
        """
        ### 스택을 이용한 문자 제거
        - `char`이 스택에 쌓여 있는 문자이고, 뒤에 문자가 남아있는 경우(카운터가 0 이상) 쌓아둔 것을 없앤다.
        - `seen` : 이미 처리된 문자 여부 확인 
        """
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1  # 현재문자를 사용하기 때문에 1씩 카운팅 감소하기
            if char in stack: # 스택에 있는 경우 다시 유턴..
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거한다.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                # 1. 현재 문자(char)이 이전 문자(stack[-1])보다 앞선 문자 인 경우
                # 2. 뒤에 붙일 문자가 아직 남아 있는 경우 (`counter`가 0개 이상인 경우)
                stack.pop() # 스택에서 쌓아둔걸 제거 한다.
            stack.append(char)
            seen.add(char)
        return ''.join(stack) # 문자열로 변환


        


solution = Solution
solution.removeDuplicateLetters_2(solution, s1)
solution.removeDuplicateLetters_2(solution, s2)