def heapify(alist, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and alist[i] < alist[l]:
        largest = l
    if r < n and alist[largest] < alist[r]:
        largest = r
    if largest != i:
        swap(alist, largest, i)
        heapify(alist, n, largest)

        def heapSort(alist):
            n = len(alist)
            for i in range(n, -1, -1):
                heapify(alist, n, i)
            for i in range(n - 1, 0, -1):
                swap(alist, 0, i)
                heapify(alist, i, 0)

                alist = [2, 5, 3, 8, 6, 5, 4, 7]
                heapSort(alist)
                print("Sorted array is")
                print(alist)