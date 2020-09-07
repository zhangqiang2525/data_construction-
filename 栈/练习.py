# from 栈.stack import Stack


# 1.实现一个栈
# class Stack(object):
#     def __init__(self):
#         self.items = []
#
#     def push(self, x):
#         return self.items.append(x)
#
#     def delete(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[len(self.items) - 1]
#
#     def isEmpty(self):
#         return True if len(self.items) == 0 else False
#
#     def size(self):
#         return len(self.items)


# 用栈实现括号匹配
# def parChecker(symbolString):
#     s = Stack()
#     flag = True
#     index = 0
#     while index < len(symbolString) and flag:
#         if symbolString[index] == '(':
#             s.push(symbolString[index])
#         else:
#             if s.isEmpty():
#                 flag = False
#             else:
#                 s.delete()
#         index += 1
#
#     if s.isEmpty() and flag:
#         return True
#     return False
#
#
#
# l = parChecker('((())))')
# print(l)


# class Solution:
#     def calPoints(self, ops):
#         stack = []
#         for i in ops:
#             if i != 'C' and i != 'D' and i != '+':
#                 stack.append(int(i))
#             elif i == 'D':
#                 if stack:
#                     stack.append(stack[-1] * 2)
#             elif i == '+':
#                 if len(stack) > 1:
#                     stack.append(stack[-1] + stack[-2])
#             else:
#                 if stack:
#                     stack.pop()
#
#         return sum(stack)
#
#
# s = Solution()
# print(s.calPoints(["5", "2", "C", "D", "+"]))


# class Solution(object):
#     def calPoints(self, ops):
#         """
#         :type ops: List[str]
#         :rtype: int
#         """
#         score = [0, 0]
#         for c in ops:
#             if c.lstrip('-').isdigit():
#                 score.append(int(c))
#             elif score:
#                 score = {
#                     "+": score + [score[-2] + score[-1]],
#                     "C": score[:-1],
#                     "D": score + [2 * score[-1]]
#                 }.get(c)
#         return sum(score)
#
#
# s = Solution()
# print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.B[-1]


s = MinStack()
s.push(-3)
s.push(0)
s.push(2)
print(s.A)
print(s.B)
print(s.min())
s.pop()
print(s.A)
print(s.B)