"""
[17]
전화 번호 문자 조합
2에서 9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력해라.

1(---) 2(abc) 3(def)
4(ghi) 5(jkl) 6(mno)
7(pqrs) 8(tuv) 9(wxyz)
* 0(+) #



- 난이도 : ⭐️⭐️
- 시간복잡도 : 


[EXAMPLE 1]
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Explanation : 2는 abc, 3은 def 가 가능하므로 각각 한문자씩 9개의 조합이 가능하다.

[EXAMPLE 2]
Input: digits = ""
Output: []

[EXAMPLE 3]
Input: digits = "2"
Output: ["a","b","c"]
"""

class Solution:
    def letterCombinations(self, digits: str):
        def dfs(index, path):
            """
            `index`: 입력 자릿수 , `path` : 추가된 키 배열(ex) ab)
            1. 입력값 자릿수 단위 반복
            2. 끝까지 탐색하면 백트래킹
            """
            # 자릿수 동일할 떄까지 재귀 호출 반복 후 결과 추가 리턴
            if len(path) == len(digits): # path('ad') 길이와 digits('23')길이가 같은 경우
                result.append(path) # result에 path 추가 (['ad', 'ae', 'af' ... ])
                return

            # 입력값 자릿수 단위 반복 (재귀 탐색)
            for i in range(index, len(digits)): # 23일 경우 : 0, 1, 2
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]: # j = d, e, f 
                    dfs(i + 1, path + j)
        
        # 예외 처리
        if not digits:
            return []
        
        # 키판 배열
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "") # Index, path

        return result

sol = Solution()
print(sol.letterCombinations("23"))