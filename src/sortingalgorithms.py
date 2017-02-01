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


print(insertion_sort(array))
print(insertion_sort_faster(array))
print(selection_sort(array))



