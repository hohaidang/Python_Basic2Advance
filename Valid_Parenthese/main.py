class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        hs_tbl = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c not in hs_tbl and len(stack) != 0:
                # close bracket
                pop = stack.pop()
                if hs_tbl[pop] != c:
                    return False
                # else: continue
            elif c in hs_tbl:
                # open bracket
                stack.append(c)
            else:
                return False
        return True if not stack else False


a = Solution()
print(a.isValid("{[]}"))