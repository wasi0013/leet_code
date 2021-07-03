class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        nodes_a = set()
        nodes_b = set()
        while a or b:
            if a:
                if a in nodes_b:
                    return a
                nodes_a.add(a)
                a = a.next
            if b:
                if b in nodes_a:
                    return b
                nodes_b.add(b)
                b = b.next
        return Non
    
    e
