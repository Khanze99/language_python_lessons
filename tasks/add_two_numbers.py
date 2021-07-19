

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_list_node(self, numbers: list):
        self.val = numbers[0]
        prev = self

        for i, n, in enumerate(numbers[1:]):
            new = ListNode(val=n)
            prev.next = new
            prev = new

        return self

    def __repr__(self):
        return f"ListNode object val: {self.val}"


class Solution:  # 68 ms 14.3 mb memory usage
    # TODO need clear code
    """
    listNode = [7, 0, 8] -> 807
    return list [ListNode]
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1.next, l2.next
        l_node_result = ListNode(val=l1.val + l2.val)
        prev = l_node_result
        while True:
            if not node1 and not node2:
                if prev.val > 9:
                    new = ListNode()
                    new.val = prev.val // 10
                    prev.val %= 10
                    prev.next = new
                break

            if node1 and node2:
                new = ListNode()
                new.val = node1.val + node2.val

                if prev:
                    if prev.val > 9:
                        new.val += prev.val // 10
                        prev.val %= 10
                    prev.next = new
                prev = new

                node1, node2 = node1.next, node2.next

            elif not node1 or not node2:
                if node1:
                    new = ListNode(val=node1.val)
                if node2:
                    new = ListNode(val=node2.val)
                if prev:
                    if prev.val > 9:
                        new.val += prev.val // 10
                        prev.val %= 10
                    prev.next = new
                prev = new

                if node1 or node2:
                    if (node1 and not node1.next) or (node2 and not node2.next):
                        new = ListNode()
                        new.val = prev.val // 10
                        prev.val %= 10
                        if new.val:
                            prev.next = new
                    if node1:
                        node1 = node1.next
                    if node2:
                        node2 = node2.next

        return l_node_result


class SolutionD():  # 64 ms 14.2 mb memory usage

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_node = ListNode()
        prev = res_node
        carry = 0

        while l1 or l2 or carry:

            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            carry, out = divmod(val1+val2+carry, 10)

            prev.next = ListNode(val=out)
            prev = prev.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return res_node.next
