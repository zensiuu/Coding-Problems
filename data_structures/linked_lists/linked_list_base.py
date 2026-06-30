"""
Base ListNode class and helpers for all linked list exercises.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    """Convert a Python list to a linked list. Returns head."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def list_to_array(head):
    """Convert a linked list to a Python list."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def print_list(head):
    """Print a linked list as a -> b -> c -> None"""
    vals = list_to_array(head)
    print(" -> ".join(str(v) for v in vals) + " -> None")
