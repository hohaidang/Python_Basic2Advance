table_convert = {'I' : 1,
                 'V' : 5,
                 'X' : 10,
                 'L' : 50,
                 'C' : 100,
                 'D' : 500,
                 'M' : 1000}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        temp = table_convert['M']
        for c in s:
            if(temp < table_convert[c]):
                num -= 2*temp;
            num += table_convert[c]
            temp = table_convert[c]
        return num;


a = Solution();
print(a.romanToInt("XL"));
