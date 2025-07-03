import sys 
def delete(array,index):
    length=len(array)
    tempArray=[0 for _ in range(length-1)]
    for i in range(0,length):
        if i <index:
            tempArray[i]=array[i]
        if i>index:
            tempArray[i-1]=array[i]
    return tempArray
def main():
    scores=[90,70,50,80,60,85]
    index=int(input("please enter the index to be deleted:\n"))
    scores=delete(scores,index)

    length=len(scores)
    for i in range(0,length):
        print(scores[i],"",end="")
if __name__=="__main__":
    main()       