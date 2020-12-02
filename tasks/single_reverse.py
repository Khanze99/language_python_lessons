# доделать задачку

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


head = Node(1)

v2 = Node(2)
head.next = v2

v3 = Node(3)
v2.next = v3

v4 = Node(4)
v3.next = v4

v5 = Node(5)
v4.next = v5

# на входе [1, 2, 3, 4, 5]
# на выходе [5,4,3,2,1]


def printLinkedList(head: Node):
  ret = []

  while head != None:
    ret.append(head.value)
    head = head.next

  print(ret)


def reverse(head: Node) -> Node:

    if head.next is not None:

        return reverse(head.next)

    if head.next is None:
        return head


print(reverse(head).value)
