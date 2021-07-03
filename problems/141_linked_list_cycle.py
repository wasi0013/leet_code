class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = set()
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False

