class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]

        row = len(grid)
        col = row

        inbound = lambda r, c : 0 <= r < row and 0 <= c < col
        
        if grid[0][0] == 1:
            return -1

        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        count = 0
    
        while q:
            n = len(q)
            count += 1
                                         
            for i in range(n):
                cell = q.popleft()
                
                if cell[0] == row - 1 and cell[1] == col - 1:
            
                    return count

                

                for i, j in directions:
                    nr = i + cell[0]
                    nc = j + cell[1]
                
                    if inbound(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            


        return -1