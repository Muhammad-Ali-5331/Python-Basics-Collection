from collections import deque
class Solution:
    def Apply2sCompliment(self, b):
        for k in range(31, -1, -1):
            if b[k] == '1': break
        for l in range(k - 1, -1, -1):
            b[l] = '1' if b[l] == '0' else '0'
        return b

    def Bits(self, num):
        bits = deque(bin(abs(num))[2:])
        while len(bits) < 32: bits.appendleft('0')
        return self.Apply2sCompliment(bits) if num < 0 else bits

    def getSum(self, a: int, b: int) -> int:
        x = self.Bits(a)
        y = self.Bits(b)
        SUM = ["0"] * 32
        carry = 0
        for j in range(31, -1, -1):
            val1 = int(x[j])
            val2 = int(y[j])
            carrySum = val1 + carry
            if carrySum > 1:
                carry = 1
                val1 = 0
            elif carrySum == 1:
                carry = 0
                val1 = 1
            lowerRes = val1 + val2
            if lowerRes > 1:
                carry = 1
            elif lowerRes == 1:
                SUM[j] = '1'
        if SUM[0] == '1':
            SUM = self.Apply2sCompliment(SUM)
            res = int("".join(SUM), 2) * -1
            return res
        return int("".join(SUM), 2)


obj = Solution()
num1 = -100
num2 = -1
print(obj.getSum(num1, num2))