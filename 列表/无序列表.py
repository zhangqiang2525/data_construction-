from 列表.节点 import Node


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_Empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp


my_list = UnorderedList()
print(my_list.add(31))
print(my_list.add(77))
print(my_list.add(21))
