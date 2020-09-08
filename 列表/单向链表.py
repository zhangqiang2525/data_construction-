# 构建节点
class Node(object):
    def __init__(self, value):
        # 元素域
        self.value = value

        # 链接域
        self.next = None


class LinkedListOneway(object):
    def __init__(self, node=None):
        """
        定义头节点
        :param node:
        """
        self.__head = node

    def __len__(self):
        """
        计算链表长度
        :return:
        """
        # 游标，用来遍历列表
        cur = self.__head

        # 记录遍历次数
        count = 0
        while cur:
            count += 1
            cur = cur.next

        return count

    def is_empty(self):
        """
        头节点不为None则不为空
        :return: True:链表为空 False:链表不为空
        """
        return self.__head == None

    def add(self, value):
        """
        头插法
        先让新节点的next指向头节点所指向的方向，
        再将头节点替换为新节点，
        :param value:
        :return:
        """
