"""
Date - 17.05.2024

DSA Topic - Queue

Given an integer k, and queue of integers, reverse first k  elements of the queue.

1. Create an empty stack
2. Iterate for range k, dequeue from queue and push into stack
3. while stack not empty enqueue back to queue.
4. Iterate over range queue.size - k (which is remaining items from original), dequeue from
   queue and enqueue back to queue.

"""

from Stack.stack_using_array_wol import stack
from Queue_DS.Q import Que


def reverse_first_k_elements(q: Que, k: int) -> Que:
    aux_stack = stack()

    for i in range(k):
        aux_stack.push(q.dequeue())

    while not aux_stack.is_empty():
        q.enqueue(aux_stack.pop())

    for i in range(q.size() - k):
        q.enqueue(q.dequeue())

    print(f'First {k} elements reversed Q --> {q}')
    return q


if __name__ == '__main__':
    Q = Que()
    Q.enqueue(10)
    Q.enqueue(20)
    Q.enqueue(30)
    Q.enqueue(40)
    Q.enqueue(50)
    Q.enqueue(60)
    Q.enqueue(70)
    Q.enqueue(80)

    reverse_first_k_elements(Q, 4)


