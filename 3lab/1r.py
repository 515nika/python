def intersect_recursive(list1, list2, index=0, result=None):
    if result is None:
        result = []
    if index >= len(list1):
        return result
    if list1[index] in list2 and list1[index] not in result:
        result.append(list1[index])
    return intersect_recursive(list1, list2, index + 1, result)

print(intersect_recursive([1, 2, 3, 4], [2, 3, 4, 6, 8]))
print(intersect_recursive([5, 8, 2], [2, 9, 1]))
print(intersect_recursive([5, 8, 2], [7, 4]))