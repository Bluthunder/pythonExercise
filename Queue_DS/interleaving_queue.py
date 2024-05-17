"""
Date - 16.05.2024

DSA - QUEUE

Given a queue of integer rearrange the elements by interleaving the first half of list
with second half of the list


1.Push the first half elements of the queue to stack.
2.Enqueue back the stack elements.
3.Dequeue the first half elements of the queue and enqueue them back.
4.Again push the first half elements into the stack.
5.Interleave the elements of queue and stack.
"""
from Stack.stack_using_array_wol import stack
from Q import Que as kyu


def interleaveQ(q):
    mid = q.size() // 2

    Stk = stack()

    # Insert 1st half in stack

    for i in range(mid):
        Stk.push(q.dequeue())

    # Enqueue to Queue_DS from stack

    while not Stk.is_empty():
        q.enqueue(Stk.pop())

    # 1st Half dequeue and enqueue

    for _ in range(0, mid):
        q.enqueue(q.dequeue())

    # push 1st half to stack again

    for _ in range(0, mid):
        Stk.push(q.dequeue())

    while not Stk.is_empty():
        q.enqueue(Stk.pop())
        q.enqueue(q.dequeue())

def interleave_BF(q):
    m = Q.size() // 2

    q1 = kyu()
    q2 = kyu()
    resQ = kyu()

    for i in range(m):
        q1.enqueue(Q.dequeue())

    for i in range(m):
        q2.enqueue(Q.dequeue())

    # print(f' Q1 - {q1}')
    # print(f' Q2 - {q2}')

    for i in range(m):
        resQ.enqueue(q1.dequeue())
        resQ.enqueue(q2.dequeue())

    print(f' FINAL Q -- {resQ}')
    return resQ


if __name__ == '__main__':
    Q = kyu()

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)

    # print(f'Original Q - {Q}')
    # interleaveQ(Q)
    # print(f' Interleaved Q - {Q}')

    interleave_BF(Q)



