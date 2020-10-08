"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.
​
As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.
​
The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)
​
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"
​
class QueueTwoStacks:
    def __init__(self):
        # Your code here
        # hold all of the elements that get enqueued 
        self.in_stack = Stack()
        # hold all of the elements in reverse order for when we need 
        # to dequeue 
        self.out_stack = Stack()
        
    def enqueue(self, item):
        # Your code here
        self.in_stack.push(item)
​
    def dequeue(self):
        # Your code here
        # check if our out_stack is empty 
        if len(self.out_stack.data) == 0:
            # if it's empty, add all of the elems from in_stack to our 
            # out_stack, reversing the order of elems along the way 
            while len(self.in_stack.data) > 0:
                self.out_stack.push(self.in_stack.pop())
            # check if our out_stack has elements to pop 
            if len(self.out_stack.data) == 0:
                raise IndexError("Can't dequeue from an empty queue") 
        # pop from our out_stack 
        return self.out_stack.pop()
