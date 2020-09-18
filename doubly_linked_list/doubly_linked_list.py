"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
    

        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return
        elif self.length == 1:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value
        else:
            old_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return
        old_tail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return old_tail.value
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return old_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if (self.head is None and self.tail is None) or (self.length == 1):
            return
        else:
            if (node.next is not None):
                node.prev.next = node.next
                node.next.prev = node.prev.next
            if node is self.tail:
                self.tail = node.prev
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if (self.head is None and self.tail is None) or (self.length == 1):
            return
        else:
            if (node.prev is not None):
                node.next.prev = node.prev
                node.prev.next = node.next.prev
            if node is self.head:
                self.head = node.next
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if (self.head is None and self.tail is None):
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            if node.prev is not None:
                node.next.prev = node.prev
                node.prev.next = node.next.prev
            if node.next is not None:
                if node.prev is None:
                    node.next.prev = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev.next
            if node is self.head:
                self.head = node.next
            if node is self.tail:
                self.tail = node.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value