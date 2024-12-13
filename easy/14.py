class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        flag = True
        output = ''

        if '' in strs:
            return ''

        if len(strs) == 1:
            return strs[0]

        for output_len in range(1, 200):
            prefix = strs[0][:output_len]

            for i in range(1, len(strs)):
                if strs[i][:output_len] == prefix:
                    continue
                else:
                    flag = False
            if flag:
                output = prefix
                flag = True
                if prefix == strs[0]:
                    return output
            else:
                return output