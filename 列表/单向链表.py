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
        return self.__head is None

    def add(self, value):
        """
        头插法
        先让新节点的next指向头节点所指向的方向，
        再将头节点指向新节点
        要先保证原链表的链不断,因此下面两段代码的顺序不能改变，否则头节点后面的链会丢失
        node.next = self.__head
        self.__head = node
        :param value:
        :return:
        """
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def append(self, value):
        """
        尾插法
        先遍历找到None值
        :param value:
        :return:
        """
        node = Node(value)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, value):
        # 应对特殊情况
        if pos <= 0:
            self.add(value)
        elif pos > len(self) - 1:
            self.append(value)
        else:
            node = Node(value)
            prior = self.__head
            count = 0
            # 在插入位置的前一个节点停下
            while count < (pos - 1):
                prior = prior.next
                count += 1
            # 先将插入节点与节点后的节点连接，防止链表断掉，先链接后面的，再链接前面的
            node.next = prior.next
            prior.next = node

    def remove(self, value):
        cur = self.__head
        prior = None
        while cur:
            if value == cur.value:
                # 判断此节点是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    prior.next = cur.next
                break
            # 还没找到节点，有继续遍历
            else:
                prior = cur
                cur = cur.next

    def search(self, value):
        cur = self.__head
        while cur:
            if value == cur.value:
                return True
            cur = cur.next
        return False

    def traverse(self):
        cur = self.__head
        while cur:
            print(cur.value)
            cur = cur.next