def merge_sort(alist):
    n = len(alist)
    if n > 1:
        mid = n // 2
        alist1 = alist[:mid]
        alist2 = alist[mid:]

        merge_sort(alist1)
        merge_sort(alist2)

        i = 0
        j = 0
        while i < mid and mid + j < n:
            if alist1[i] < alist2[j]:
                alist[i + j] = alist1[i]
                i += 1
            else:
                alist[i + j] = alist2[j]
                j += 1

        while i < mid:
            alist[i + j] = alist1[i]
            i += 1

        while mid + j < n:
            alist[i + j] = alist2[j]
            j += 1
            alist = [5, 2, 8, 6]
            merge_sort(alist)
            print(alist)