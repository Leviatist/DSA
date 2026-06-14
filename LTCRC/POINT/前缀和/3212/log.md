# info 
|rating|time  |med|all|
|---   |---   |---|---|
|1673  |11m30s|28 |55 |
# 二维矩阵前缀和
对二维矩阵的前缀和计算，可以抽象为如下逻辑：

`G[r][c] = G[r][c-1] + G[r-1][c] + G[r][c] - G[r-1][c-1]`

注意这里 `G[r][c]` 是尚未前缀和的矩阵元素。
# 代码思路及修改汇总
## 初始
### 思路
题目要求 X，Y 频次相同，一个直观的想法就是 O(ne2) 建立两个矩阵，之后 O(1)诸个判断并统计。

建立矩阵的需要用到前缀和，对二维矩阵的前缀和。
### V1
#### 代码
```python
class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        gridX = [[int(grid[0][0]=='X') for _ in grid[0]] for _ in grid]
        gridY = [[int(grid[0][0]=='Y') for _ in grid[0]] for _ in grid]
        for i in range(1, len(grid[0])):
            gridX[0][i] = int(grid[0][i]=='X') + gridX[0][i-1]
            gridY[0][i] = int(grid[0][i]=='Y') + gridY[0][i-1]
        for r in range(1, len(grid)): 
            for c in range(len(grid[0])):
                if c==0:
                    gridX[r][c] = int(grid[r][c]=='X')+gridX[r-1][c]
                    gridY[r][c] = int(grid[r][c]=='Y')+gridY[r-1][c]
                else:
                    gridX[r][c] = gridX[r][c-1]+gridX[r-1][c]-gridX[r-1][c-1]+int(grid[r][c]=='X') 
                    gridY[r][c] = gridY[r][c-1]+gridY[r-1][c]-gridY[r-1][c-1]+int(grid[r][c]=='Y')
        # print(gridX)
        # print(gridY)
        for r in range(len(grid)): 
            for c in range(len(grid[0])):
                if gridX[r][c]>0 and gridX[r][c]==gridY[r][c]:
                    cnt+=1    
        return cnt
```
#### 结果
速度很慢，大概是最快的提交的 $\dfrac{1}{2}$，用了 2100 ms

我不能接受。

具体分析一下，其实是因为：

1. 之前赋值用了强制类型转换，写成三元表达式可能快一些。
2. 不停地判断，其实可以在建表时一次写好。

小改一下。
### V2（三元表达式/赋值逻辑/减少一次循环）
#### 代码
```python
class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        gridX = [[1 if grid[r][c]=='X' else 0 for c in range(len(grid[0]))] for r in range(len(grid))]
        gridY = [[1 if grid[r][c]=='Y' else 0 for c in range(len(grid[0]))] for r in range(len(grid))]
        for i in range(1, len(grid[0])):
            gridX[0][i] = gridX[0][i] + gridX[0][i-1]
            gridY[0][i] = gridY[0][i] + gridY[0][i-1]
        for r in range(1, len(grid)): 
            for c in range(len(grid[0])):
                if c==0:
                    gridX[r][c] = gridX[r][c] + gridX[r-1][c]
                    gridY[r][c] = gridY[r][c] + gridY[r-1][c]
                else:
                    gridX[r][c] = gridX[r][c-1] + gridX[r-1][c] - gridX[r-1][c-1] + gridX[r][c] 
                    gridY[r][c] = gridY[r][c-1] + gridY[r-1][c] - gridY[r-1][c-1] + gridY[r][c]
        # print(gridX)
        # print(gridY)
        for r in range(len(grid)): 
            for c in range(len(grid[0])):
                if gridX[r][c]>0 and gridX[r][c]==gridY[r][c]:
                    cnt+=1    
        return cnt
```
#### 结果
修改的地方在于：
1. 我对 GridX 和 GridY 在生成的时候对每个值进行了赋值，避免了后续的赋值。（第一次没想到是因为没想到可以直接初始化，我潜意识里觉得初始化所有值和用某个值初始化，前者的时间开销更小）
2. 最后一次循环可以删去。
3. 判断的逻辑 从 `if c==0:` 改到了 `if c!=0:`，这样就很好了。

简洁多了也好看多了。

提速大概 33%，从 2100 ms -> 1360 ms.
### V3 (空间优化)
突然想到，矩阵里的数字其实是只用到上一行和本行的，所以其实开两个 $O(n^{\frac{1}{2}})$ 的空间就好了。
```python
class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        idr = 1
        gx = [1 if r=='X' else 0 for r in grid[0]]
        gy = [1 if r=='Y' else 0 for r in grid[0]]
        for c in range(1, len(grid[0])):
            gx[c] += gx[c-1]
            gy[c] += gy[c-1]
        while True:
            for c in range(len(grid[0])):
                if gx[c]==gy[c] and gx[c]>0:
                    cnt+=1
            if idr==len(grid):
                break
            cx = [0]*len(grid[0])
            cy = [0]*len(grid[0])
            cx[0] = 1+gx[0] if grid[idr][0] == 'X' else gx[0]
            cy[0] = 1+gy[0] if grid[idr][0] == 'Y' else gy[0]
            for c in range(1, len(grid[0])):
                cx[c] = cx[c-1] + gx[c] - gx[c-1] + (1 if grid[idr][c]=='X' else 0)
                cy[c] = cy[c-1] + gy[c] - gy[c-1] + (1 if grid[idr][c]=='Y' else 0)
            gx = cx 
            gy = cy
            idr += 1
        return cnt
```
# 杂项
在这份代码中，我使用了相对规范的命名，如 gridX 和 gridY.

这位我带来了困扰，我将若干个 grid 打成了 gird，导致纠错花了很长时间。

我之后的命名应该摆一些。