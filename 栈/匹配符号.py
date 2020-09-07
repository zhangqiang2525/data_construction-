from 栈.stack import Stack


# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         if symbolString[index] in '({[':
#             s.push(symbolString[index])
#
#         else:
#             if s.is_empty():
#                 balanced = False
#             else:
#                 top = s.delete()
#                 if not matches(top, symbolString[index]):
#                     balanced = False
#
#         index += 1
#
#     if s.is_empty() and balanced:
#         return True
#     return False
#
#
# def matches(open, close):
#     opens = '({['
#     closers = ')}]'
#     return opens.index(open) == closers.index(close)
#
#
# l = parChecker('{([])}')
# print(l)
