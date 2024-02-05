def insertion_sort(lst):
    i=1
    while i<len(lst):
        x=lst[i]
        j=i-1
        while j>=0 and lst[j]>x:
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=x
        i=i+1
    return lst
lsts=insertion_sort([1,4,2,6,7,23,4,7,8])
print(lsts)
