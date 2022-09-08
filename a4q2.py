##Nmae:Jinhao Zhong NSID:jiz263  student#:11204178 Cmpt145  L05
import TStack as TStack
import TQueue as TQueue

stack = TStack.create()
queue = TQueue.create()
expression = input('enter:')

def if_balance(expression):

    for x in expression:
        if x is '(' or x is '[' or x is '{':
            TStack.push (stack, x)
        elif x is ')' or x is ']' or x is '}':
            TQueue.enqueue(queue, x)

    if TStack.size(stack)==TQueue.size(queue)!=0:
        if TStack.pop(stack) is '(':
            if TQueue.is_empty(queue):
                return False
            elif TQueue.dequeue(queue) is  not ')':
                return False
            return True

        if TStack.pop(stack) is '[':
            if TQueue.is_empty(queue):
                return False
            elif TQueue.dequeue(queue) is  not ']':
                return False
            return True

        if TStack.pop(stack) is '{':
            if TQueue.is_empty(queue):
                return False
            elif TQueue.dequeue(queue) is  not '}':
                return False
            return True
    elif TStack.size(stack)==TQueue.size(queue)==0:
        return True
    else:
        return False



if if_balance(expression) :
    print('True')
else:
    print('False')

