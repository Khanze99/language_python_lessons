

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# l1 = ListNode(val=2, next=ListNode(4, next=ListNode(3, next=None)))
# l2 = ListNode(val=5, next=ListNode(6, next=ListNode(4, next=None)))
l1 = ListNode(val=9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=None)))))))))
l2 = ListNode(val=9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=None))))

# sum [7, 0, 8] -> 807
# return list [ListNodes]


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_node_result = ListNode()
        node1, node2 = l1, l2
        prev = None
        while True:
            if not l_node_result.val:
                val = l1.val + l2.val
                l_node_result.val = val
                prev = l_node_result
                node1, node2 = node1.next, node2.next
                if not node1 and not node2:
                    break
                continue

            if not node1 or not node2:
                break

            new = ListNode()
            new.val = node1.val + node2.val

            if prev:
                if prev.val > 9:
                    new.val += prev.val // 10
                    prev.val %= 10
                prev.next = new
            prev = new

            node1, node2 = node1.next, node2.next

        return l_node_result
