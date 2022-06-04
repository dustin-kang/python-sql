"""
[020]
유효한 괄호
- 문제 : 괄호로 된 입력값이 올바른지 판별하기
- 난이도 : ⭐️

[EXAMPLE 1]
Input: s = "()"
Output: true

[EXAMPLE 2]
Input: s = "()[]{}"
Output: true

[EXAMPLE 3]
Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s : str):
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char not in table:  # '[{('
                stack.append(char)
            elif not stack or table[char] != stack.pop(): # )}] -> ({[ == stack element
                # 스택이 없는 경우 : '}'
                return False
        return len(stack) == 0 # 스택 리스트가 비었을 경우 True

sol = Solution

e1 = "[]"
e2 = "[](){}"
e3 = "{)" # table[char] != stack.pop()
e4 = "{()}" 
e5 = "}" # Not Stack
e6 = "{" # len(stack) == 0
print(sol.isValid(sol, e6))