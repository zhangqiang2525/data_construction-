from 栈.stack import Stack


# def divideBy2(decNumber):
#     remstack = Stack()
#
#     while decNumber > 0:
#         rem = decNumber % 2
#         remstack.push(rem)
#         decNumber = decNumber // 2
#
#     binString = ""
#     while not remstack.is_empty():
#         binString = binString + str(remstack.delete())
#
#     return binString
#
#
# print(divideBy2(9))


def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remstack.is_empty():
        newString = newString + digits[remstack.delete()]

    return newString


print(baseConverter(233, 8))



