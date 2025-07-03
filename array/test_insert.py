import sys 
def insert(array,score,insertingindex):
    length=len(array)
    tempArray=[0 for _ in range(0,length)]

    for i in range(0,length):
        if i>insertingindex:
            tempArray[i]=array[i]
        else:
            tempArray[i+1]=array[i]
    tempArray[insertingindex]=score 
    return tempArray
def main():
    score=[90,70,50,80,60,85]
    scores=insert(score,75,2)
    length=len(scores)
    for i in range(0,length):
        print(scores[i],"",end="")
if __name__=="__main__":
    main()