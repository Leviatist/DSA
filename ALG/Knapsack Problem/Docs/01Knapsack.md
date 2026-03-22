# 01背包(0/1 Knapsack)(递归无优化/记忆化递归/动态规划/例题)
## 前言
+ 代码及原始文档见[我的Github仓库](https://github.com/Leviaist/DSA)，持续更新
## 问题背景
+ 对于容量为c的背包，有一些物件需要装到背包中。
+ 每个物件具有两个属性，w(weight,权重)和v(value,价值)。
+ 每个物件若放到背包中，会占用大小为w的背包容量，同时提供大小为v的价值。
+ 01背包问题希望最终装进背包的物体总价值最大。
## 解法
### 递归无优化
#### 代码
```python
def  knapsack_01_recursive(w,v,c):
    '''
    Parameters:
    w: List[float] - List of item weights.
    v: List[float] - List of item values.
    c: float - Maximum capacity of the knapsack.
    
    Returns:
    float - The maximum value that can be obtained with the given weight limit.

    Complexity Analysis:
    Tc:O(2^n),Sc:O(2^n)
    '''
    if len(w)==1:
        return v[0] if c>=w[0] else 0
    else:
        branch_0 = knapsack_01_recursive(w[1:],v[1:],c-w[0])+v[0] if c>=w[0] else 0
        branch_1 = knapsack_01_recursive(w[1:],v[1:],c)
        return max(branch_0,branch_1)
    #return (v[0] if c>=w[0] else 0) if len(w)==1 else (max(knapsack_01_recursive(w[1:],v[1:],c-w[0])+v[0] if c>=w[0] else 0,knapsack_01_recursive(w[1:],v[1:],c)))
```
#### 解析
对于每个要被装进背包的物件：
+ 如果这是最后一件物品(`if len(w)==1:`)：
    - **如果背包还有容量**：装入背包，返回物品的价值
    - **如果背包无容量**：不装入背包，返回0
+ 如果这不是最后一件物品(`else:`)，则考虑两个分支：
    - **分支一**：如果背包还有容量，则装入背包，剔除这件物品，容量减去物品的权重，尝试将剩下的物品装入容量减少后的背包，如果背包没有容量，返回0
    - **分支二**：剔除这件物品，尝试将剩下的物品装入背包

时间复杂度:$O(2^n)$,空间复杂度:$O(2^n)$。

时空复杂度都很差，唯一的优点(如果算)可能是代码可以用一行写完(见被注释掉的那一行)。
### 记忆化递归
#### 代码
```python
def knapsack_01_memo(w,v,c,memo=None):
    '''
    Parameters:
    w: List[float] - List of item weights.
    v: List[float] - List of item values.
    c: float - Maximum capacity of the knapsack.
    memo: dict, optional - A dictionary used to store results of subproblems to avoid redundant calculations.
    
    Returns:
    float - The maximum value that can be obtained with the given weight limit.

    Complexity Analysis:
    Tc:O(2^n),Sc:O(2^n)
    '''
    memo = {} if memo is None else memo
    if (len(w), c) in memo:
        return memo[(len(w), c)]
    if len(w)==1:
        memo[len(w),c] = v[0] if c>=w[0] else 0
        return v[0] if c>=w[0] else 0
    else:
        branch_0 = knapsack_01_memo(w[1:],v[1:],c-w[0],memo)+v[0] if c>=w[0] else 0
        branch_1 = knapsack_01_memo(w[1:],v[1:],c,memo)
        memo[len(w),c] = max(branch_0,branch_1)
        return max(branch_0,branch_1)
```
#### 解析
思路与递归思路基本相同，区别在于:
+ 定义了一个字典memo，对于每个以`len(w),c`为标签的情况，都存储了该情况的计算结果
+ 因为对于每个`len(w),c`的情况都只需要计算一次，因此时间空间复杂度都为$O(nc)$
+ Python在函数中传递可变对象（e.g. List,dict）时，传送的是对可变对象的一个引用，任何修改作用于原对象。
### 动态规划
#### 代码
```python
def knapsack_01_dp(w, v, c):
    '''
    Parameters:
    w: List[float] - List of item weights.
    v: List[float] - List of item values.
    c: float - Maximum capacity of the knapsack.
    
    Returns:
    float - The maximum value that can be obtained with the given weight limit.

    Complexity Analysis:
    Tc:O(nc),Sc:O(nc)
    '''
    n = len(w)
    dp = [[0] * (c + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(c + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][c]
```
#### 解析
+ 关于动态规划数组dp的理解:
    - `dp[i][j]`意为:在背包中还有前i件物品可供选择，容量剩余为j的情况下，能得到的最大价值
    - 本代码中开辟了$nc$的空间，但开辟$c$的空间也能解决问题

### 测试用例及代码
```python
tc = [[1,2,3,4,5],[2,4,4,5,6],6]
r = knapsack_01_recursive(*tc)
r = knapsack_01_memo(*tc)
r = knapsack_01_dp(*tc)
print(r)    
```

## 例题
### 例题1
题目：[Leetcode Problem 416](https://leetcode.cn/problems/partition-equal-subset-sum/description/)

解法：
```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def knapsack_01_dp(w, v, c):
            '''
            Parameters:
            w: List[float] - List of item weights.
            v: List[float] - List of item values.
            c: float - Maximum capacity of the knapsack.
            
            Returns:
            float - The maximum value that can be obtained with the given weight limit.

            Complexity Analysis:
            Tc:O(nc),Sc:O(nc)
            '''
            n = len(w)
            dp = [[0] * (c + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(c + 1):
                    if w[i - 1] <= j:
                        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
                    else:
                        dp[i][j] = dp[i - 1][j]
            return dp[n][c]
        return sum(nums)%2 == 0 and knapsack_01_dp(nums,nums,sum(nums)/2)==sum(nums)/2
```