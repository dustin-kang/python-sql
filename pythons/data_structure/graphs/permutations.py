"""
[46]
순열
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.


- 난이도 : ⭐️⭐️
- 시간복잡도 : 


[EXAMPLE 1]
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

[EXAMPLE 2]
Input: nums = [0,1]
Output: [[0,1],[1,0]]

[EXAMPLE 3]
Input: nums = [1]
Output: [[1]]
"""

import itertools


class Solution:
    def permute(self, nums: list(int())):
        """
        DFS를 활용한 순열 생성
        """
        results = []
        prev_elements = []

        def dfs(elements):
            # 만약 마지막 리프노드일 때 결과값 추가
            if len(elements) == 0: # n : []
                results.append(prev_elements[:]) # [[p = 1,2,3], ]

            # 계속해서 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:] # n : [123] - [23] - [3]
                next_elements.remove(e) # n : [23] - [3] - []

                prev_elements.append(e) # n : [23] , p : [1] - n : [3] , p : [12] - n : [] , p : [123]
                dfs(next_elements) 
                prev_elements.pop() 

        dfs(nums) # START!
        return results

    def permute2(self, nums: list(int())):
        """
        `itertools` 모듈을 사용한 방법
        구현의 효율성 및 성능 향상을 위해 사용
        - 튜플 형식으로 경우의 수를 뽑을 수 있다.
        `itertools.permutations(list, 하나씩 뽑을 갯수)`
        """
        # return list(itertools.permutations(nums))
        return list(map(list, itertools.permutations(nums)))
