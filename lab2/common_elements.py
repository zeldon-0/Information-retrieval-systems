def common(list1, list2):
    result = []
    for item1 in list1:
        if item1 in list2 and item1 not in result:
            result.append(item1)

    for item2 in list2:
        if item2 in list1 and item2 not in result:
            result.append(item2)

    return result
