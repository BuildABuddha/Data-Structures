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

    def __repr__(self):
        temp_list = []

        current_node = self.head
        while current_node:
            temp_list.append(str(current_node.value))
            current_node = current_node.next

        return f"Head: {self.head.value}\nTail: {self.tail.value}\n" + ", ".join(temp_list)
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value=value, next=self.head, prev=None)

        if self.head is None:
            self.tail = new_node
        
        self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            # Empty list!
            return None
        elif self.head is self.tail:
            # 1 object in list!
            head_val = self.head.value
            self.head = None
            self.tail = None
        else:
            # 2 or more objects in list!
            head_val = self.head.value
            self.head = self.head.next
            self.head.prev = None

        self.length -= 1
        return head_val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value=value, next=None)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
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
        if self.head is None:
            return None
        elif self.head is self.tail:
            tail_val = self.tail.value
            self.tail = None
            self.head = None
        else:
            tail_val = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1
        return tail_val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if not node is self.head and self.length > 1:
            self.delete(node)

            self.head.prev = node
            node.prev = None
            node.next = self.head

            self.head = node
            self.length += 1
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if not node is self.tail and self.length > 1:
            self.delete(node)

            self.tail.next = node
            node.next = None
            node.prev = self.tail

            self.tail = node
            self.length += 1

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head.value
        else:
            max_val = self.head.value
            current_node = self.head.next
            while current_node:
                if current_node.value > max_val:
                    max_val = current_node.value
                current_node = current_node.next

            return max_val
