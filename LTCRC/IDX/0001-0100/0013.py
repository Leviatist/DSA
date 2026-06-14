# 06-14-2026 https://leetcode.cn/problems/roman-to-integer/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        for i in range(len(s)):
            if s[i] == 'M':
                r += 1000
            elif s[i] == 'D':
                r += 500
            elif s[i] == 'C':
                if i==len(s)-1:
                    r += 100 
                elif s[i+1] == 'D' or s[i+1] == 'M':
                    r -= 100
                else:
                    r += 100
            elif s[i] == 'L':
                r += 50 
            elif s[i] == 'X':
                if i==len(s)-1:
                    r += 10 
                elif s[i+1] == 'L' or s[i+1] == 'C':
                    r -= 10
                else:
                    r += 10
            elif s[i] == 'V':
                r+= 5 
            else:
                if i==len(s)-1:
                    r += 1 
                elif s[i+1] == 'X' or s[i+1] == 'V':
                    r -= 1
                else:
                    r += 1
        return r 