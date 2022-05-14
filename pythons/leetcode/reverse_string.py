"""
344
문자열을 뒤집는 함수 작성하기

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

# Swap을 통한 투 포인터 방법
s = ["h","e","l","l","o"]

left, right = 0, len(s) -1
while left < right: # 왼쪽이 더 클때 까지 반복
    s[left], s[right] = s[right], s[left] # SWAP
    left += 1 # 첫 문자부터 점점 인덱스 증가
    right -= 1 # 마지막 문자부터 점점 인덱스 감소



# 굉장히 파이썬 다운 방법
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()