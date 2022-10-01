"""
1694. 重新格式化电话号码
简单题
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        s, lst = [], []
        for x in number:
            if x.isdigit():
                s.append(x)

        n, i = len(s), 0
        while n > 0:
            if n == 4:
                lst.append(''.join(s[i:i + 2]))
                lst.append(''.join(s[i + 2:i + 4]))
                break
            lst.append(''.join(s[i:i + 3]))
            i += 3
            n -= 3

        return '-'.join(lst)
