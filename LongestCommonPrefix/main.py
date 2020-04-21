class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        temp_str = strs[0]
        i = 0
        j = 1
        dataRet = '';
        while (i < len(temp_str)):
            flag = 0
            for idx in range(1, len(strs)):
                if temp_str[0:i + 1] == strs[idx][0:i + 1]:
                    flag = 1
                else:
                    return dataRet
            if flag:
                dataRet = temp_str[0:i + 1]
            i += 1
        return dataRet



a = Solution();
print(a.longestCommonPrefix(["",""]))
