from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            
            if head == self.current:
                self.current = self.storage.tail 

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        list_buffer_contents.append(self.current.value)

        if self.current.next:
            _next = self.current.next

        else:
            _next = self.storage.head

        while _next is not self.current:
            list_buffer_contents.append(_next.value)
            if _next.next:
                _next = _next.next
            else:
                _next = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1

        if self.current is self.capacity:
            self.current = 0

    def get(self):
        arr = []
        for i in self.storage:
            if i is not None:
                arr.append(i)

        return arr
