## Arrays
### List
- Order matters
- All elements are important
- Able to store multiple different data types
- Mutable

### Tuple / Array
- Order matters
- Fixed number of elements of the same data type
- Immutable
- Limitations
  - If the list is unordered, searching is slow
    - Best: Item found is the first in the list
    - Worse: Going through all items before the item is found
  - If the list is ordered, insertion / deletion is slow
    - Best: No shifting of items is needed before operations
    - Worse: Need to shift existing items before operation

### Sets
- Order does not matter
- Mutable
- Can't have the same element twice
- Able to store multiple different data types