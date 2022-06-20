"""
[200]
섬의 개수
1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 갯수를 계산하라.
(연결되어 있는 1의 덩어리 수를 구하라.)


- 난이도 : ⭐️⭐️
- 시간복잡도 : 


[EXAMPLE 1]
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

[EXAMPLE 2]
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:
    def numIslands(self, grid: list(list(str))):
            """
            DFS로 그래프 탐색하는 풀이 방법
            """
            # 예외처리
            if not grid:
                return 0

            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1': # 행, 열 단위로 육지를 찾다가 육지(1)가 발견되는 경우
                        self.dfs(grid, i, j) # 탐색을 시작한다.
                        count += 1 # 모든 육지 탐색 후 카운트 1 증가
            return count

    def dfs(self, grid, i, j):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
                return
        grid[i][j] = '0' # 이미 방문 했던 곳은 0으로 처리한다.

        # 동서남북 탐색
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


class Solution2:
    def numsIslands(self, grid: list(list(str))):
        """
        중첩 함수
        `numIslands()` 함수 내에 `dfs()`가 중첩 함수로 들어갔다.
        - 부모 함수에서 선언한 변수도 유효한 범위 내에서 사용할 수 있다.
        """
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
            grid[i][j] = '0' # 이미 방문 했던 곳은 0으로 처리한다.

            # 동서남북 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': # 행, 열 단위로 육지를 찾다가 육지(1)가 발견되는 경우
                    dfs(i, j) # 탐색을 시작한다.
                    count += 1 # 모든 육지 탐색 후 카운트 1 증가
        return count



            
