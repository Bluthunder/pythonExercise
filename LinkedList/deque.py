"""
Date - 12.05.2024

DSA - Queue

This is Queue implementation using python collections class - deque
Deque object supports below methods

1. append(x) : Add x to right side
2. appendleft(x) : Add x to left side
3. clear() : Remove all Elemenets from deque leaving with length 0
4. copy() :  Create a shallow copy of deque
5. count(x) :  Count the number of elements equal to x
6. pop() :  Remove and return element from right side
7. popleft() :  Remove and return element from left side of deque
8. maxlen() : Maximum size of deque or None if unbounded



"""

from collections import deque


class Q:
    queue = deque(maxlen=5)
    queue.append(2)
    queue.append(4)
    queue.append(6)
    queue.append(8)
    queue.append(10)
    print(queue)

    queue.appendleft(0)

    print(queue)

    queue.popleft()
    print(queue.count(2))

