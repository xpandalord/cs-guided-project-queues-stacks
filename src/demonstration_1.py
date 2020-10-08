"""
You've encountered a situation where you want to easily be able to pull the
largest integer from a stack.
​
You already have a `Stack` class that you've implemented using a dynamic array.
​
Use this `Stack` class to implement a new class `MaxStack` with a method
`get_max()` that returns the largest element in the stack. `get_max()` should
not remove the item.
​
*Note: Your stacks will contain only integers. You should be able to get a
runtime of O(1) for push(), pop(), and get_max().*
"""
class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
​
    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)
​
    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
​
        return self.items.pop() # O(1)
​
    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]
​
class MaxStack:
    def __init__(self):
        # Your code here
        self.stack = Stack()
        # this variable will always hold on to our max value in the stack
        # we want the history of all maxes in our stack  
        self.maxes = Stack() 
​
    def push(self, item):
        """Add a new item onto the top of our stack."""
        # Your code here
        self.stack.push(item)
        # check to see if `self.maxes` needs to be updated 
        if len(self.maxes.items) == 0 or self.maxes.peek() < item:
            self.maxes.push(item)
​
    def pop(self):
        """Remove and return the top item from our stack."""
        # Your code here
        # peek the top element of the stack 
        # if it matches our `self.max`, we need to update `self.max` 
        # to be the max of the remaining stack elements
        if self.stack.peek() == self.maxes.peek():
            self.maxes.pop() 
​
        return self.stack.pop()
​
    def get_max(self):
        # Your code here
        # we can't mess with the order of elements in our `self.stack` 
        # use a sort that copies the input before sorting them 
        # return sorted(self.stack.items)[-1] # O(n log n)
        # use the `max` function 
        # return max(self.storage.items) # O(n)
        return self.maxes.peek()
​
​
max_stack = MaxStack()
max_stack.push(98)
max_stack.push(15)
max_stack.push(27)
max_stack.push(101)
max_stack.push(25)
​
print(max_stack.get_max())
print(max_stack.pop())
print(max_stack.pop())
print(max_stack.get_max())