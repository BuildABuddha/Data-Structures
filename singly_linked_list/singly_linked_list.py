class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node=next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            head_val = None
        else:
            if self.head is self.tail:
                self.tail = None

            head_val = self.head.value
            self.head = self.head.next_node

        self.length -= 1

        return head_val

    def contains(self, value):
        contains_value = False

        current_node = self.head

        while current_node:
            if current_node.value == value:
                contains_value = True
                break
            current_node = current_node.next_node

        return contains_value

    def get_max(self):
        if self.head is None:
            max_val = None
        elif self.length == 1:
            max_val = self.head.value
        else:
            max_val = self.head.value
            current_node = self.head.next_node
            while current_node:
                if current_node.value > max_val:
                    max_val = current_node.value
                current_node = current_node.next_node

        return max_val