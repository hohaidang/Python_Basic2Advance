class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:] # remove '0b'


a = Solution()
bin = a.addBinary("1111", "0010")
print("HelloWorld")