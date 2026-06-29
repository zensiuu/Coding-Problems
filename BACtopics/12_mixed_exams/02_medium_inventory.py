"""
MIXED EXAMS - MEDIUM 1: Inventory Management
Hint: combine records + search + sort

You manage a store inventory. Each item is a dict:
  {"id": int, "name": str, "price": float, "qty": int}

Write:
  1. add_item(inventory, item) — appends item to inventory
  2. find_by_name(inventory, name) — returns first item matching name
  3. items_below_qty(inventory, threshold) — returns list of items
     with qty < threshold (reorder alert)
  4. total_value(inventory) — sum of price * qty for all items

Examples:
  inv = []
  add_item(inv, {"id":1,"name":"Pen","price":1.5,"qty":100})
  items_below_qty(inv, 50) -> []
"""

def add_item(inventory, item):
    pass

def find_by_name(inventory, name):
    pass

def items_below_qty(inventory, threshold):
    pass

def total_value(inventory):
    pass


if __name__ == "__main__":
    inv = []
    add_item(inv, {"id": 1, "name": "Pen", "price": 1.5, "qty": 100})
    add_item(inv, {"id": 2, "name": "Notebook", "price": 3.0, "qty": 30})
    add_item(inv, {"id": 3, "name": "Eraser", "price": 0.5, "qty": 200})
    assert len(inv) == 3
    assert find_by_name(inv, "Notebook")["id"] == 2
    assert find_by_name(inv, "None") is None
    assert len(items_below_qty(inv, 50)) == 1
    assert total_value(inv) == 1.5*100 + 3.0*30 + 0.5*200
    print("All tests passed!")
