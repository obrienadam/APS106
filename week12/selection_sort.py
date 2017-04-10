def selection_sort(items):
    if len(items) == 1:
        return items
    else:
        return [items.pop(items.index(max(items)))] + selection_sort(items)

def merge_sort(items):
    if len(items) == 1:
        return items
    else:
        l1 = merge_sort(items[:len(items)//2])
        l2 = merge_sort(items[len(items)//2:])

        l = []
        while l1 and l2:
            l.append(l1.pop(0) if l1[0] > l2[0] else l2.pop(0))

        l += l1
        l += l2

        return l

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 2, 5, 7]
    print(selection_sort(items))