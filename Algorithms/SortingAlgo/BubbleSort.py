def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-j):
            if items[j]>items[j+1]:
                items[j],items[j+1]=items[j+1],items[j]
    return items
Item=[3,4,6,3,2,89,5,23,56]
Nm=bubble_sort(Item)
print(Nm)

