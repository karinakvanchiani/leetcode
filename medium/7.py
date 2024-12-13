class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        ans = []
        if int(x) < 0:
            ans.append('-')
            x = x[1:]
            
        if len(x) == 1:
            ans.append(x)
        else:
            for i in range(len(x) - 1, 0, -1):
                if x[-1] == '0':
                    x = x[:-1]
                else:
                    ans.append(x[i])
            ans.append(x[0])
        
        x = int(''.join(ans))
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        return x