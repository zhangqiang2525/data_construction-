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
        self.length = 0

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
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
        self.length += 1

    def append(self, value):
        """
        尾插法
        先遍历找到结尾的None值
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
        self.length += 1

    def insert(self, pos, value):
        """
        随机插入
        :param pos: 位序
        :param value: 值
        :return:
        """
        # 应对特殊情况
        if pos <= 0:
            self.add(value)
        elif pos > self.length - 1:
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
        self.length += 1

    def remove(self, value):
        """
        删除元素
        :param value: 要删除的值
        :return:
        """
        cur = self.__head
        prior = None    # 该游标为cur的前一个节点x
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
        self.length -= 1

    def search(self, value):
        """
        查找节点是否存在
        :param value:
        :return:
        """
        cur = self.__head
        while cur:
            if value == cur.value:
                return True
            cur = cur.next
        return False

    def travel(self):
        """
        遍历链表
        :return:
        """
        cur = self.__head
        while cur:
            print(cur.value)
            cur = cur.next
        print(self.length)


