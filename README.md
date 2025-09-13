# Linked Lists and Recursion Lab

A Python implementation of a linked list with recursive operations for managing employee IDs.

## What This Does

This lab demonstrates:
- **Linked List**: Dynamic data structure for storing integer IDs
- **Recursion**: Elegant solutions for traversing and manipulating the list
- **Real-world application**: Employee roster management system

## Files

- `linked_list.py` - Node and LinkedList classes with recursive methods
- `main.py` - Demo script showing all functionality
- `test_linked_list.py` - Unit tests to verify implementation

## Key Features

### LinkedList Methods
- `insert_at_front(data)` - Add new node at beginning (O(1))
- `insert_at_end(data)` - Add new node at end (O(n))
- `recursive_sum()` - Sum all values using recursion
- `recursive_search(target)` - Find value using recursion
- `recursive_reverse()` - Reverse list in-place using recursion
- `display()` - Print list contents

### Recursive Logic
- **Sum**: Returns 0 for empty, otherwise `current + sum(rest)`
- **Search**: Returns False for empty, True if found, otherwise search rest
- **Reverse**: Swap pointers recursively until list is reversed

## How to Run

```bash
# Run the demo
python main.py

# Run tests
python -m pytest test_linked_list.py
# or
python test_linked_list.py
```

## Example Output

```
=== Linked Lists and Recursion Lab Demo ===

1. Created an empty LinkedList
Empty list

2. Inserting sample data...
Current list:
30 -> 20 -> 10 -> 5 -> None

4. Testing recursive sum...
Sum of all elements: 65

5. Testing recursive search...
Search for 20: Found
Search for 100: Not found

6. Testing recursive reverse...
List after reversal:
5 -> 10 -> 20 -> 30 -> None
```

## Learning Goals

- Understand node-based data structures
- Practice recursive problem-solving
- Apply data structures to real scenarios (employee management)
- Write clean, well-documented code

## Lab Complete ✅

All recursive methods implemented and tested successfully!