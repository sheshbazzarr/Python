import sys
def sort(array):
    length=len(array)
    for i in range(0,length-1):
        insert_element=array[i]
        insert_postion=i
        for j in range(insert_postion-1,-1,-1):
            if insert_element<array[j]:
                array[j+1]=array[j]
                insert_postion-=1
        array[insert_postion]=insert_element
def main():
    scores=[80,70,60,50,95]
    sort(scores)
    for score in scores:
        print(score,"",end="")
if __name__=="__main__":
    main()