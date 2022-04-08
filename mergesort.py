def merge_sort(l, start, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(l, start, mid)
        merge_sort(l, mid, end)
        merge_list(l, start, mid, end)
 
def merge_list(l, start, mid, end):
    left = l[start:mid]
    right = l[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            l[k] = left[i]
            i = i + 1
        else:
            l[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            l[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            l[k] = right[j]
            j = j + 1
            k = k + 1
l = list(map(int,input("enter the value in list : ").strip().split()))
merge_sort(l, 0, len(l))
print('Sorted list: ', end='')
print(l)