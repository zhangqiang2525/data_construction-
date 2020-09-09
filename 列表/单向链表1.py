# 创建节点
class Node(object):
    def __init__(self, item):
        self.element = item
        self.next = None


# 创建单链表类
class SingleLinkList(object):
    def __init__(self):
        self.header = None
        self.length = 0

    # 1、判断是否为空
    def is_empty(self):
        if self.header is None:
            return True
        else:
            return False

    # 2、头部插入
    def add(self, node):
        if self.is_empty():
            self.header = node
        else:
            nodes = Node(node)
            nodes.next = self.header
            self.header = nodes
        self.length += 1

    # 3、尾部插入
    def append(self, node):
        current_Node = self.header
        if self.is_empty():
            self.add(node)
        else:
            while current_Node.next is not None:
                current_Node = current_Node.next
            current_Node.next = node
            self.length += 1

    # 4、指定位置插入
    def insert(self, node, index):
        current_Node = self.header

        if index > self.length + 1 or index <= 0:
            while (index > self.length + 1 or index <= 0):
                print("你要插入的位置不对，请重选位置:")
                index = eval(input())

        if index == 1:
            self.add(node)
        elif index == 2:
            node.next = self.header.next
            self.header.next = node
            self.length += 1
        else:
            for i in range(1, index - 1):
                current_Node = current_Node.next
            node.next = current_Node.next
            current_Node.next = node
            self.length += 1

    # 5、遍历
    def travel(self):
        current_Node = self.header
        if self.length == 0:
            print("目前链表没有数据！")
        else:
            print("目前链表里面的元素有:", end=" ")
            for i in range(self.length):
                print("%s " % current_Node.element, end=" ")
                current_Node = current_Node.next
            print("\n")

    # 6、排序不用交换节点的位置，只需要交换节点上的数据值
    def list_sort(self):
        for i in range(0, self.length - 1):
            current_Node = self.header
            for j in range(0, self.length - i - 1):
                if current_Node.element > current_Node.next.element:
                    temp = current_Node.element
                    current_Node.element = current_Node.next.element
                    current_Node.next.element = temp

                current_Node = current_Node.next

    # 7、按索引删除
    def delete(self, index):
        if index <= 0 or index > self.length:
            while (index <= 0 or index > self.length):
                print("你输入的下标不对，请重新输入需要删除的值的下标：")
                index = eval(input())
            #   return
        else:
            if index == 1:
                self.header = self.header.next
                currentNode = self.header
            elif index == 2:
                current_Node = self.header
                current_Node.next = current_Node.next.next
            else:
                current_Node = self.header
                for i in range(1, index - 1):
                    current_Node = current_Node.next
                current_Node.next = current_Node.next.next
        self.length -= 1

    # 8、查找是否包含,并返回下标
    def isContain(self, num):
        contain = 0
        current_Node = self.header
        for i in range(self.length):
            if current_Node.element == num:
                print("%d在链表中%d处\n" % (num, i + 1))  # i+1是在正常人认为的位置处，程序员一般是从0开始算起
                contain = 1
            current_Node = current_Node.next
        if contain == 0:
            print("%d不在链表中\n" % num)

    # 9、根据下标找节点
    def searchNodeByIndex(self, index):
        current_Node = self.header
        if index <= 0 or index > self.length:
            while (index <= 0 or index > self.length):
                print("你输入的下标不对，请重新输入:")
                index = eval(input())
            #   return 0
        if index > 0 or index <= self.length:
            for i in range(index - 1):
                current_Node = current_Node.next
            return current_Node

    # 10、根据下标修改节点的值
    def Alert(self, index, num):  # index定义为下标
        current_Node = self.header
        if index <= 0 or index > self.length:
            print("你输入的下标不对，请重新输入!\n")
        else:
            for i in range(index - 1):
                current_Node = current_Node.next
