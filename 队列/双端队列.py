class Deque(object):
    def __init__(self):
        self.items = []

    def addFront(self, x):
        self.items.append(x)

    def addRear(self, x):
        self.items.insert(0, x)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def size(self):
        return len(self.items)


# 回文检测器
def check_string(target_string):
    s = Deque()
    flag = True
    for i in target_string:
        s.addRear(i)
    while s.size() > 1 and flag:
        first = s.removeRear()
        last = s.removeFront()
        if last != first:
            flag = False

    return flag


l = check_string('radars')
print(l)

