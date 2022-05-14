"""
005

가장 긴 팰린드롬 부분 문자열

가장 긴 팰린드롬 문자열을 출력해라

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer. "aba"도 정답으로 인정

Input: s = "cbbd"
Output: "bb"

** 최장 공통 문자열(Longest Common Substring) 풀이 방식
- Dynamic Programming
- Two Pointer 
    - 홀수로 확장하는 경우 1-3-5 (b -> bab)
    - 짝수로 확장하는 경우 2-4-6 (ba -> baba)

** 문제 풀이
1. 예외 처리 필터링 (이건 백퍼 가능하다)
2. 처음 부터 끝까지 우측으로 이동
"""
s = "babad"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str: # 중첩함수 expand 사용
            while left >= 0 and right <= len(s) and s[left] == s[right -1]:
                left -= 1
                right += 1
            return s[left + 1 : right - 1]
        
        # 1. 예외처리 ) 해당 사항이 없는 경우 빠르게 리턴
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        
        # 2. 슬라이딩 윈도우 ) 처음부터 끝까지 우측으로 이동
        for i in range(0, len(s) - 1):
            result = max(result, # 가장 긴 것
                        expand(i, i+1), # 홀수 포인터 확장 "b"
                        expand(i, i+2), # 짝수 포인터 확장 ""
                        key=len)
        return result


func  = Solution()
print(Solution.longestPalindrome(func, s))

