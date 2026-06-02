    
class ListNode:
    def __init__ (self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
            # dummy node
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        # return value of i'th node
        current = self.head.next
        count = 0 
        while current != None:
            if count == index:
                return current.val
            current = current.next
            count += 1 
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        # update the pointer for the old head
        new_node.next = self.head.next
        self.head.next = new_node
        # if head was empty
        if not new_node.next:
            self.tail = new_node
         
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        i = 0 
        current = self.head
        while i < index and current:
            current = current.next
            i += 1
        if current and current.next:
            if current.next == self.tail:
                # update tail?
                self.tail = current
            # bypass the target node 
            current.next = current.next.next
            return True
        return False
            

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = [ ]
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
