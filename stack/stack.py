"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from linked_list import Node
from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
        return value

    def pop(self):
        if self.size > 1:
            removed = self.storage.tail.value
            self.storage.remove_tail()
            self.size -= 1
            return removed
        elif self.size == 1:
            removed = self.storage.head.value
            self.storage.remove_head()
            self.size -= 1
            return removed
        else:
            pass

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
#         return value

#     def pop(self):
#         if self.size > 0:
#             removed = self.storage[self.size - 1]
#             self.storage.pop(self.size - 1)
#             self.size -= 1
#             return removed
#         else:
#             pass
