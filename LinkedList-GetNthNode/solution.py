from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None:
        raise Exception('List is empty')
    i = 0
    while node is not None:
        if i == index:
            return node
        node = node.next
        i += 1
    raise Exception("Index out of range")
  
