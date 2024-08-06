class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    '''
    head
   ↓                                        BEFORE
   1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9

                            head
                            ↓
    ┌→ 1 → 2 → 3 → 4 → 5 → 6     7 → 8 → 9 ─┐     AFTER
    │                                       │
    └───────────────────────────--──────────┘
    '''
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the list and make it circular
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        current.next = head  # Make it circular
        
        # Step 2: Find the new tail and new head
        k = k % length  # In case k is greater than the length of the list
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None  # Break the circle
        
        return new_head

# Helper function to convert list to linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linkedlist_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

# Example usage
solution = Solution()
head = list_to_linkedlist([1, 2, 3, 4, 5])
k = 2
rotated_head = solution.rotateRight(head, k)
print(linkedlist_to_list(rotated_head))  # Output: [4, 5, 1, 2, 3]
