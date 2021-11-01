
test1, pos1 = [3, 2, 0, -4], 1
test2, pos2 = [3, 2, 0, -4], 1


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head.next
        while True:
            if slow.next:
                return True

i = 0
prev = ListNode(x=test1.pop(0))
first = prev

while test1:
    x = test1.pop(i)
    prev.next = ListNode(x=x)
    prev = prev.next

print(first.val, first.next.val)
print(prev.val, prev.next)


print(Solution().hasCycle(ListNode(x=1)))