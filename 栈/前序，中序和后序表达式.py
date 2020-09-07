from 栈.stack import Stack
import string


# 中序 ==》后序
# def infixToPostfix(infixexpr):
#     prec = {}
#     prec['*'] = 3
#     prec['/'] = 3
#     prec['+'] = 2
#     prec['-'] = 2
#     prec['('] = 1
#     s = Stack()
#     postfixList = []
#     tokenList = infixexpr.split()
#     for token in tokenList:
#         if token in string.ascii_uppercase or token.isdigit():  # 遍历token如果'A'<=token<='Z'则计数+1
#             postfixList.append(token)
#
#         elif token == '(':
#             s.push(token)
#
#         elif token == ')':
#             top_token = s.delete()
#             while top_token != '(':
#                 postfixList.append(top_token)
#                 top_token = s.delete()
#
#         else:
#             while (not s.is_empty()) and (prec[s.peek()] >= prec[token]):
#                 postfixList.append(s.delete())
#             s.push(token)
#
#     while not s.is_empty():
#         postfixList.append(s.delete())
#
#     return " ".join(postfixList)
#
# s = infixToPostfix('( A + B ) * ( C + D )')
# print(s)


# 计算后序表达式
# def postfixeval(postficexpr):
#     s = Stack()
#
#     token = postficexpr.split()
#     for i in token:
#         if i.isdigit():
#             s.push(int(i))
#
#         else:
#             items2 = s.delete()
#             items1 = s.delete()
#             result = doMath(i, items1, items2)
#             s.push(result)
#
#     return s.delete()
#
#
# def doMath(i, i1, i2):
#     if i == '+':
#         return i1 + i2
#
#     elif i == '-':
#         return i1 - i2
#
#     elif i == '*':
#         return i1 * i2
#
#     elif i == '/':
#         return i1 / i2
#
#
# s = postfixeval(' 7 8 + 3 2 / ')
# print(s)



