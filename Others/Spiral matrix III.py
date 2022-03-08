#https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total = rows * cols
        step = 1
        inc = 1
        dirns = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir_idx = 0
        res = [[rStart, cStart]]
        
        
        while(len(res) < total):
            for i in range(inc):
                rStart = (rStart) + dirns[dir_idx][0]
                cStart = (cStart) + dirns[dir_idx][1]
                
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    res.append([rStart, cStart])
            
            dir_idx = (dir_idx + 1) % 4
            
            if step % 2 == 0:
                inc += 1
            
            step += 1
            
        return res
