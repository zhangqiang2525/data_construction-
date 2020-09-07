class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        添加操作
        :param item: 添加元素
        :return: None
        """
        return self.items.insert(0, item)

    def dequeue(self):
        """
        移除元素
        :return:
        """
        return self.items.pop()

    def is_empty(self):
        return True if len(self.items) == 0 else False

    def size(self):
        return len(self.items)


# q = Queue()
# print(q.is_empty())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(q.is_empty())
# print(q.items)
# q.dequeue()
# print(q.items)