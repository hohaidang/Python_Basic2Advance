class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True


        hs_tbl = {'{': '}',
                  '[': ']',
                  '(': ')'}
        list = []
        for c in s:
            if (c not in hs_tbl) and (len(list) != 0):
                # close bracket
                pop = list.pop()
                if hs_tbl[pop] != c:
                    return False;
                else:
                    continue
            elif c in hs_tbl:
                list.append(c)
            else:
                return False
        if not list:
            return True
        else:
            return False


a = Solution()
print(a.isValid("{[]}"))