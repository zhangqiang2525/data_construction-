# 方法一
class Stack(object):
    def __init__(self):
        """
        创建一个空列表
        """
        self.items = []

    def push(self, x):
        """
        :param x:添加元素
        :return: 返回items
        """
        return self.items.append(x)

    def delete(self):
        """
        :return:返回删除的元素
        """
        return self.items.pop()

    def peek(self):
        """
        查看栈顶元素
        :return:
        """
        return self.items[len(self.items) - 1]

    def is_empty(self):
        """
        判空操作
        :return:
        """
        if len(self.items) == 0:
            return True
        return False

    def items_size(self):
        """
        栈的长度
        :return:
        """
        return len(self.items)


# 方法二：将列表头作为栈的顶端
# class Stack1(object):
#     def __init__(self):
#         """
#         创建一个空列表
#         """
#         self.items = []
#
#     def push(self, x):
#         """
#         每次往列表头插入一个元素
#         :param x:
#         :return:
#         """
#         return self.items.insert(0, x)
#
#     def delete_x(self):
#         """
#         每次删除列表头的第一个元素
#         :return:
#         """
#         return self.items.pop(0)
#
#     def peek(self):
#         """
#         返回栈顶元素，因为列表头为栈顶因此只需要返回itms[0]
#         :return:
#         """
#         return self.items[0]
#
#     def is_empty(self):
#         """
#         判空操作
#         :return:
#         """
#         if len(self.items) == 0:
#             return True
#         return False
#
#     def items_size(self):
#         """
#         栈的长度
#         :return:
#         """
#         return len(self.items)


