def  knapsack_01_recursive(w, v, c):
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

def knapsack_01_memo(w, v, c,memo=None):
    '''
    Parameters:
    w: List[float] - List of item weights.
    v: List[float] - List of item values.
    c: float - Maximum capacity of the knapsack.
    memo: dict, optional - A dictionary used to store results of subproblems to avoid redundant calculations.
    
    Returns:
    float - The maximum value that can be obtained with the given weight limit.

    Complexity Analysis:
    Tc:O(nc),Sc:O(nc)
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

tc = [[1,2,3,4,5],[2,4,4,5,6],6]
r = knapsack_01_recursive(*tc)
r = knapsack_01_memo(*tc)
r = knapsack_01_dp(*tc)
print(r)    