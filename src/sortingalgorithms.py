# Implementing sorting algorithms using pseudo code from Wikipedia
# Simple sort: Insertion sort, Selection sort
# Efficient sort: Merge sort, Heapsort, Quicksort
# Bubble sort and variants: Bubble sort, Shellsort, Comb sort
# Distribution sort: Counting sort, Bucket sort, Radix sort

array = [5, 4, 8, 7, 9, 0, 1, 3, 6, 2]


# Insertion sort
def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


def insertion_sort_faster(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0  and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a


# Selection sort
def selection_sort(a):
    n = len(a)
    for j in range(0, n - 1):
        i_min = j
        for i in range(j + 1, n):
            if a[i] < a[i_min]:
                i_min = i
        if i_min != j:
            a[j], a[i_min] = a[i_min], a[j]
    return a


# Merge sort
def merge_sort(m):
    if len(m) <= 1:
        return m

    left = []
    right = []
    for i, x in enumerate(m):
        if i <= len(m)//2:
            left.append(x)
        else:
            right.append(x)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    while left:
        result.append(left[0])
        left.pop(0)
    while right:
        result.append(right[0])
        right.pop(0)
    return result


# print(insertion_sort(array))
# print(insertion_sort_faster(array))
# print(selection_sort(array))
# print(merge_sort(array))