# ---------- STACK ----------
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
# Result = ['A', 'B', 'C']

# Peek - Back Out
print(stack[-1])
# Result = ['A', 'B', 'C']

# Pop
print(stack.pop())
# Result = ['A', 'B']

# Is Empty
print("Not Empty" if bool(stack) else "Empty")
# Result = Not Empty

# Size
print(len(stack))
# Result = 2

# ---------- QUEUE ----------
from collections import deque
queue = deque()

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
# Result = deque(['A', 'B', 'C'])

# Peek - Front Out
print(queue[0])
# Result = deque(['A', 'B', 'C'])

# Dequeue
print(queue.popleft())
# Result = deque(['B', 'C'])

# Rotate
queue.rotate()
# Result = deque(['C', 'B'])

# ---------- Stuff to consider studying ----------
# Reading - Reverse Order
# Reading - Intervals
# Reading - Specific Range
# Reading - Something that doesn't exist (if applicable)
# Add - At the end
# Add - In front
# Add - In the middle
# Add - In missing index (1, 3, 4) so insert in index 2
# Edit - Something that exists
# Edit - Something that doesn't exist
# Edit - In front
# Edit - In the end
# Edit - Everything
# Delete - Everything
# Delete - Specific thing
# Delete - In front
# Delete - In the end
# Delete - Something that doesn't exist
# Sorting keys / Re-ordering something