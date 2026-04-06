class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
               return '0'

        n1 = len(num1)
        n2 = len(num2)

        res = [0] * (n1 +n2)

        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):

                multi = int(num1[i]) * int(num2[j])

                pos1 = i+j+1
                pos2 = i+j

                total = multi + res[pos1]

                res[pos1] = total % 10
                res[pos2] +=  total // 10

        return "".join(map(str,res)).lstrip('0')               
        