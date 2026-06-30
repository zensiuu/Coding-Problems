"""
QUEUES - EASY 2: Circular Queue
Hint: use a fixed-size list with front and rear pointers that wrap around

Implement a class CircularQueue(k) with:
  - enqueue(val): insert, return True on success, False if full
  - dequeue(): remove, return True on success, False if empty
  - front(), rear(): get items
  - is_empty(), is_full()

Example:
  q = CircularQueue(3)
  q.enqueue(1) -> True
  q.enqueue(4) -> False (if full)
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    q = CircularQueue(3)
    print(f"enqueue 1 = {q.enqueue(1)}  expected = True")
    print(f"enqueue 2 = {q.enqueue(2)}  expected = True")
    print(f"enqueue 3 = {q.enqueue(3)}  expected = True")
    print(f"enqueue 4 = {q.enqueue(4)}  expected = False (full)")
    print(f"rear = {q.rear()}  expected = 3")
    print(f"dequeue = {q.dequeue()}  expected = True")
    print(f"enqueue 4 = {q.enqueue(4)}  expected = True")
    print(f"rear = {q.rear()}  expected = 4")
