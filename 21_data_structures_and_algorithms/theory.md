Linked Lists -> Page 12 +, remembering the notation of each operation
Singly linked list
Doubly linked list
Dynamic Array
Hash
Tree
Recursion 
Graph
Searching Algorithms
Sorting Algorithms

Terminology to understand:
- hash
- sparse
- immutability
- performance considerations

# Implementations
Python does not directly support these structures. As such, we use lists and dictionaries to simulate these structures.

## Limitations of Lists
1. If list is unordered, searching is slow
    - Best case: Item found is the first in the list
    - Worst case: Item found is the last in the list
2. If list is ordered, insertion/deletion is slow
    - Best case: No shifting of items needed before the operation
    - Worst case: Need to shift existing items before the operation

# Data Structures
Data structures are specialised formats for organising and storing data in a computer so that it can be used efficiently.

## Stacks
A Linear Data Structure that follows the Last-In-First-Out (LIFO) principle. 
This means that data can only be added and removed at one end, the top.

Methods:
- Push 
- Peek
- Pop
- Is Empty
- Size

## Queues
A Linear Data Structure that stores items in First-In/First-Out (FIFO) manner.
It can only be inserted at the rear and removed from the front.

Methods:
- Enqueue
- Peek
- Dequeue
- Rotate (Last element will jump to the front)

## Linked Lists
A linked list consists of nodes with some sort of data, and a pointer, or link to the next node.

Properties:
- Do not have to be shifted up or down in memory when nodes are inserted or deleted
- Requires more memory to store links

Types:
- Singly linked lists: Link to the next node
- Doubly linked lists: Link to the next node and the previous node
- Circular linked lists: Singly + an additional link with the first node and the last node

Methods:
- Traversal
- Remove a node
- Insert a node
- Sort