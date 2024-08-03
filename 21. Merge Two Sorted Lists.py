# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
              
            else:
                current.next = list2
                list2 = list2.next
    
            current = current.next
    
        if list1:
            current.next = list1
        elif list2:
            current.next = list2 
            
        return dummy_head.next
        
    
def list_to_linkedlist(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in arr[1:]:
        current.next = ListNode(i)
        current = current.next
    return head

def linkedlist_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr 

s= Solution()
list1 = list_to_linkedlist([1, 2, 8])
list2 = list_to_linkedlist([1, 3, 4, 6, 7])

merge = s.mergeTwoLists(list1, list2)
print(linkedlist_to_list(merge))  # Output: [1, 1, 2, 3, 4, 4]