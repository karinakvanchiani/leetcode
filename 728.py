class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_div = []

        for num in range(left, right + 1):
            flag = True
            digits = set([*str(num)])
            if '0' in digits:
                continue
            for dig in digits:
                if num % int(dig) != 0:
                    flag = False
                    break
                    
            if flag:
                self_div.append(num)

        return self_div
                    