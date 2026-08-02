#Pre-Code Solution Setup
class singlynode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
    
# createing a linked list
def create_linked_list(arr):
    """Automatically creates and connects nodes from a list of values."""
    if not arr:
        return None
    # Creates the head node of the linked list with the first value 
    head = singlynode(arr[0])
    current = head
    
     # 2. Loop through the rest of the values and link them automatically
    for val in arr[1:]:
        current.next = singlynode(val) #create and connect the nextnode
        current = current.next #Move our pointerto next node
    return head

# creating a display funtion
def displaylinkedlist(head):
    current = head
    element = []
    while current:
        element.append(str(current.val))
        current =  current.next
    print(' --> '.join(element))
    
    
head = create_linked_list([1,2,3,3,4,5,5,6,7,7])
displaylinkedlist(head)

def deleteDuplicates(head):
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  
            else:
                current = current.next  
                
        return head
    
displaylinkedlist(deleteDuplicates(head))