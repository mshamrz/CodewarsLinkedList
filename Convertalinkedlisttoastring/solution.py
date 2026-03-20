def stringify(node):
    current = node
    result = []
    while current is not None:
        result.append(str(current.data))
        current = current.next
    result.append('None')
    return ' -> '.join(result) 
