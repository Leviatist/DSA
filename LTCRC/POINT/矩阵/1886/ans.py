class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def judge(m1, m2):
            for r in range(len(m1)):
                for c in range(len(m1)):
                    if m1[r][c]!=m2[r][c]:
                        return False 
            return True 
        def t(m):
            rt = [[0 for _ in range(len(m))] for _ in range(len(m))]
            for r in range(len(m)):
                for c in range(len(m)):
                    rt[r][c] = m[len(m)-1-c][r]
            return rt 
        for i in range(4):
            if judge(mat, target):
                return True 
            mat = t(mat)
        return False 