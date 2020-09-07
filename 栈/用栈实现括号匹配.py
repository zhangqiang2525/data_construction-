from 栈.stack import Stack


# def parChecker(symbolString):
#     s = Stack()
#     flag = True
#     index = 0
#     while index < len(symbolString) and flag:
#         if symbolString[index] == '(':
#             s.push(symbolString[index])
#         else:
#             if s.is_empty():
#                 flag = False
#             else:
#                 s.delete()
#         index += 1
#
#     if flag and s.is_empty():
#         return True
#     return False
