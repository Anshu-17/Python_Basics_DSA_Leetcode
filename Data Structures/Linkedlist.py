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
        

#traversing  and printing the linked list elements 
def traverselinkedlist(head):
    current =head
    while current:
        print(current.val)
        current = current.next


#search an element inlinked list 
def searchlinkedlist(head, target_val):
    current =  head
    while current:
        if current.val  == target_val:
            return True
        current = current.next
    return False

#search an element inlinked list and return index/node
def searchlinkedlistindexed(head, target_val):
    current =  head
    node = 0
    while current:
        if current.val  == target_val:
            return node
        current = current.next
        node += 1
    return -1

# insert a new value at givenn position
def insertnodeatpos(head, target_postion, value):
    new_node = singlynode(value)
    if target_postion == 0:
        new_node.next = head
        return new_node
    current = head
    index = 0 
    while current and index < target_postion - 1:
        current = current.next
        index += 1
    if not current:
        print(f"position {target_postion} is out of bounds")
        return head
    new_node.next = current.next
    current.next = new_node
    return head

# deleting at a given postion
def deletenodebyvalue(head, target_val):
    if not head:
        print("List is empty")
        return None
    if head.val == target_val:
        return head.next 
    current = head
    while current.next and current.next.val != target_val:
        current = current.next
    if not current.next:
        print(f"Value {target_val} not found in the list")
        return head
    current.next = current.next.next
    
    return head

    
head = create_linked_list([1,3,4,7,9,2,5])
displaylinkedlist(head)
traverselinkedlist(head)
print(searchlinkedlist(head, 9))
print(searchlinkedlist(head, 99))
print(searchlinkedlistindexed(head,5))
print(searchlinkedlistindexed(head,100))

head = insertnodeatpos(head, 3, 8)
print("\nAfter Insertion:")
displaylinkedlist(head)

head = deletenodebyvalue(head, 4)

print("\nAfter Deleting Index 4:")
displaylinkedlist(head)