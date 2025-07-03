import sys 
def search(array,value):
    length=len(array)
  
    for i in range(0,length):
        if array[i]==value:
            return i 
    return -1
def main():
    scores=[50,60,70,80,90]
    value=int(input("please enter the value you wanted to search:\n"))
    index=search(scores,value)
    if index>=0:
        print("found value",value,"the index is ",index)
    else:
        print("the value was not found",value)
    
if __name__=="__main__":
    main()