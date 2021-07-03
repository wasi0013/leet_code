class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        sorted_list = ListNode()
        l = sorted_list
        while True:
            if l1 != None and l2 != None:
                if l1.val < l2.val:
                    l.val = l1.val
                    l1 = l1.next
                else:
                    l.val = l2.val
                    l2 = l2.next                
            elif l1 != None:
                l.val = l1.val
                l1 = l1.next
            elif l2 != None:
                l.val = l2.val
                l2 = l2.next
            else:
                break
            if l1 != None or l2 != None:
                l.next = ListNode()
                l = l.next
        return sorted_list

