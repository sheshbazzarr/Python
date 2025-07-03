import sys 
def binary_search(arrays,search_value):
    length=len(arrays)
    low=0
    high=length-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if arrays[mid]==search_value:
            return mid 
        elif arrays[mid]<search_value:
            low=mid+1 
        else:
            high=mid-1
    return -1
def main():
    scores=[30,40,50,70,80,90]
    search_value =40 
    position=binary_search(scores,search_value)
    print(search_value,"position",position)
    print("-----------")
    search_value=90
    postion=binary_search(scores,search_value)
    print(search_value,"position",position)

if __name__=="__main__":
    main()