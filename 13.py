class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        skip = False
        
        for i in range(len(s) - 1, -1, -1):
            if skip:
                skip = False
                continue

            if i != 0:
                now, pred = s[i], s[i - 1]
            else:
                now, pred = s[i], 'A'
                
            if (pred == 'I' and now in ['V', 'X']) or (pred == 'X' and now in ['L', 'C']) or (pred == 'C' and now in ['D', 'M']):
                integer += mapping[now] - mapping[pred]
                skip = True
            else:
                integer += mapping[now]
                skip = False
                
        return integer
        