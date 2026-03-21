from preloaded import Node

def swap_pairs(head):
    new_head = Node(0)
    new_head.next = head
    prev = new_head
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
    return new_head.next
