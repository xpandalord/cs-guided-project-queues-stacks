import time 
from ll_queue import LLQueue
from array_queue import ArrayQueue
from collections import deque
​
n = 100000
​
AQ = ArrayQueue()
LLQ = LLQueue() 
DQ = deque()
​
start_time = time.time()
for i in range(0, n):
    AQ.enqueue(i)
end_time = time.time()
print(f"Array Queue time to enqueue: {end_time - start_time} seconds")
​
start_time = time.time()
for i in range(0, n):
    LLQ.enqueue(i)
end_time = time.time()
print(f"LLQueue time to enqueue: {end_time - start_time} seconds")
​
start_time = time.time()
for i in range(0, n):
    DQ.append(i)
end_time = time.time()
print(f"Deque time to enqueue: {end_time - start_time} seconds")
​
start_time = time.time()
for i in range(0, n):
    AQ.dequeue()
end_time = time.time()
print(f"Array Queue time to dequeue: {end_time - start_time} seconds")
​
start_time = time.time()
for i in range(0, n):
    LLQ.dequeue()
end_time = time.time()
print(f"LLQueue time to dequeue: {end_time - start_time} seconds")
​
start_time = time.time()
for i in range(0, n):
    DQ.popleft()
end_time = time.time()
print(f"Deque time to dequeue: {end_time - start_time} seconds")
