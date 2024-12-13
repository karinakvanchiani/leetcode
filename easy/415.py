class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        n1, n2 = len(num1), len(num2)
        summa = ''
        v_ume = False
        i = 0

        while i < n1 or i < n2:
            if n1 <= i:
                sum_of_digits = int(num2[i])
            elif n2 <= i:
                sum_of_digits = int(num1[i])
            else:
                sum_of_digits = int(num1[i]) + int(num2[i])

            if sum_of_digits > 9:
                if v_ume:
                    summa += str(sum_of_digits + 1)[-1]
                else:
                    summa += str(sum_of_digits)[-1]
                    v_ume = True

            else:
                if v_ume:
                    summa += str(sum_of_digits + 1)[-1]
                    if sum_of_digits < 9:
                        v_ume = False
                    else:
                        v_ume = True
                else:
                    summa += str(sum_of_digits)
            i += 1

        summa = summa + '1' if v_ume else summa
        return summa[::-1]