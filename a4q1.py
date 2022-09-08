import TStack
import TQueue

queue=TQueue.create()
stack=TStack.create()
word='URG'

"""
    Purpose
        reorder the case in txt file, make the URG case first
    Pre-conditions:
        queue: a queue created by create()
        stack: a stack created by create()
    Post-condition:
        None
    Return:
        the case in URG order
"""

##open the txt file and read it
f= open('case.txt','r').readlines()
for line in f:
    line=line.strip('\n')
    case=line.split(' ')

##split the case, URG case in stack and not URG case in queue
    for x in case:
        if word in x:
            TStack.push(stack, x)
        else:
            TQueue.enqueue(queue, x)

    ##use loop while stack is not empty, get the URG case out of stack
    while not TStack.is_empty(stack):
        x = TStack.pop(stack)
        print(x, end=' ')

    ##use looop while queue is not empty, the the not URG case out of queue
    while not TQueue.is_empty(queue):
        x = TQueue.dequeue(queue)
        print(x, end=' ')

    ##print out the case
    for i in x:
        if len(i) == 5:
            i = rstrip('\n')
    print(i)