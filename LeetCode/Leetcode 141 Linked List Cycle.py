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
    seen_nodes = set()  # Track unique node objects in memory
    while current:
        if current in seen_nodes:
            element.append(f"({current.val}) -> LOOP BACK")
            break
        seen_nodes.add(current)
        element.append(str(current.val))
        current = current.next
        
    print(' --> '.join(element))
    

#Actual Solution
def findlinkedlistcycle(head):
    if not head:
        return False
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow  = slow.next
        if slow is fast:
            return True 
    return False

#Test case for false 
head = create_linked_list([1,3,4,7,9,2,5,4])
displaylinkedlist(head)
print(findlinkedlistcycle(head))


#testcase  for true
head = create_linked_list([1, 3, 4, 7, 9, 2, 5])
tail = head
while tail.next:
    tail = tail.next  
middle_node = head.next.next  
tail.next = middle_node 
displaylinkedlist(head)
print(findlinkedlistcycle(head))



""" Time Complexity is  O(n)
     Space Complexity is 0(1) """