class ArrayQueue:
    def __init__(self):
        self.storage = []
​
    # adds a value to the back of the queue 
    def enqueue(self, value):
        self.storage.append(value) # O(1)
​
    # removes a value from the front of the queue 
    def dequeue(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop(0) # O(n)