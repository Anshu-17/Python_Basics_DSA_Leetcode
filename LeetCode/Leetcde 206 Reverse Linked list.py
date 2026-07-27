
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
    
    
head = create_linked_list([1,3,4,7,9,2,5])
displaylinkedlist(head)

#Actual Soluition
def Reverselinkedlist(head):
    current = head
    prev = None
    while current:
        new_node = current.next
        current.next = prev
        
        prev = current
        current = new_node
    return prev

reversed_list = Reverselinkedlist(head)
print("\nReversed:")
displaylinkedlist(reversed_list)