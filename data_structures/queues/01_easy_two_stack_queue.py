"""
QUEUES - EASY 1: Queue Using Two Stacks
Hint: one stack for enqueue, one for dequeue — transfer when dequeue stack is empty

Implement a class QueueTwoStacks that uses only two Python lists (stacks) to
simulate a FIFO queue. Support enqueue, dequeue, peek, and is_empty.

Example:
  q.enqueue(1), q.enqueue(2), q.dequeue() -> 1
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    q = QueueTwoStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(f"dequeue = {q.dequeue()}  expected = 1")
    print(f"peek = {q.peek()}  expected = 2")
    q.enqueue(3)
    print(f"dequeue = {q.dequeue()}  expected = 2")
    print(f"dequeue = {q.dequeue()}  expected = 3")
    print(f"is_empty = {q.is_empty()}  expected = True")
