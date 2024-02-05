def quick_sort(items,index=-1):
    len_i=len(items)

    if len_i<=1:
        return items
    pivot=items[index]
    small=[]
    large=[]
    dup=[]
    for i in items:
        if i<pivot:
            small.append(i)
        elif i>pivot:
            large.append(i)
        elif i==pivot:
            dup.append(i)
    small=quick_sort(small)
    large=quick_sort(large)

    return small + dup +large
