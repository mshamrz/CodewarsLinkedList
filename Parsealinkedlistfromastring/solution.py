class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None
    lst = list_repr.strip().split(" -> ")
    head = Node(int(lst[0]))
    current = head
    for value in lst[1:]:
        if value == 'None':
            break
        current.next = Node(int(value))
        current = current.next
    return head
