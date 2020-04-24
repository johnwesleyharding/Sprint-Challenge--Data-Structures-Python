from doubly_linked_list import DoublyLinkedList

"""
The disadvantage normally found in arrays that is overcome by the stretch goal is:
not having to append or pop incurring O(n) time complexity.  Instead changes are made
with index-based assignments O(1).  A disadvantage to this method is that the 
self.current counter could eventually overflow.
"""

class RingBuffer:
    
    def __init__(self, capacity):
        
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        if self.current == None:
            
            self.storage.add_to_head(item)
            
            if self.storage.length == self.capacity:
                
                self.current = self.storage.tail
        
        else:
        
            self.current.value = item

            if self.current == self.storage.head:

                self.current = self.storage.tail

            else:

                self.current = self.current.prev

    def get(self):
        
        list_buffer_contents = []
        _ = self.storage.tail
        
        while _.prev != None:
            
            list_buffer_contents.append(_.value)
            _ = _.prev
            
        list_buffer_contents.append(_.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    
    def __init__(self, capacity):
        
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        
        self.storage[self.current % self.capacity] = item
        self.current += 1

    def get(self):
        
        if None in self.storage:
            
            return self.storage[:self.current]
                        
        else:
            
            return self.storage
