from 队列.template import Queue


def hotpotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()


namelist = ['a', 'b', 'c']
s = hotpotato(namelist, 2)
print(s)
