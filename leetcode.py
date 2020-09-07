class Solution:
    def removeOuterParentheses(self, S):
        res, stack = "", []
        for c in S:
            # 什么情况下，某个括号要加入结果中呢？非外层括号。
            # 怎么判断是非外层括号？ 1. 左括号加入前，栈不为空。2. 右括号加入并消括号后，栈不为空
            if c == "(":
                if stack:
                    res += c
                stack.append("(")
            if c == ")":
                stack.pop()
                if stack:
                    res += c
        return res


s = Solution()
print(s.removeOuterParentheses("(()())(())"))
