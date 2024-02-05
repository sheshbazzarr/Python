def merg(A,B):
    new_list=[]
    while len(A) >0 and len(B)>0:
        if A[0]<B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)
    if len(A)==0:
        new_list=new_list+B
    if len(B)==0:
        new_list=new_list+A

    return new_list
def merg_sort(items):
    len_i=len(items)
    if len_i==1:
        return items
    mid_point=int(len_i/2)
    i1=merge_sort(items[:mid_point])
    i2=merge_sort(items[mid_point:])

    return merge(i1,i2)

