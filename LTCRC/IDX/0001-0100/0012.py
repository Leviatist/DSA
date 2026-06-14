# 06-14-2026 https://leetcode.cn/problems/integer-to-roman/description/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def f(n,b):
            k = {
                3: ['M', 'M'],
                2: ['C', 'D'],
                1: ['X', 'L'],
                0: ['I', 'V']
            }
            c = (n//pow(10, b))%10
            if c in range(1, 4):
                return k[b][0]*c 
            elif c in [4]:
                return k[b][0] + k[b][1]
            elif c in range(5, 9):
                return k[b][1] + k[b][0]*(c-5)
            elif c in [9]:
                return k[b][0] + k[b+1][0] 
            return ''
        return f(num, 3) + f(num, 2) + f(num, 1) + f(num, 0)