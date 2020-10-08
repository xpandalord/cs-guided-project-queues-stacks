from linked_list import LinkedList
​
class LLQueue:
    def __init__(self):
        self.storage = LinkedList()
​
    # adds a value to the back of the queue 
    def enqueue(self, value):
        self.storage.add_to_tail(value) # O(1)
​
    # removes a value from the front of the queue 
    def dequeue(self):
        return self.storage.remove_head() # O(1)