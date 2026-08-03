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
    
    
list1 = create_linked_list([1,2,3,4,4,7,8,8])
list2 = create_linked_list([2,3,5,6,6,8,9,9])
displaylinkedlist(list1)
displaylinkedlist(list2)

#solution
def mergeTwoLists(list1, list2):
    dummy = singlynode(0)
    current = dummy
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            current = list1
            list1 = list1.next
        else:
            current.next = list2
            current = list2
            list2 = list2.next
    current.next = list1 if list1 else list2
    return dummy.next

displaylinkedlist(mergeTwoLists(list1, list2))