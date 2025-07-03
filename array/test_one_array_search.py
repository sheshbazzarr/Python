import sys 
def reverse(array):
    length=len(array)
    middle=int(length/2)
    for i in range(middle):
        temp=array[i]
        array[i]=array[length-i-1]
        array[length-i-1]=temp
    return array 
def main():
    scores=[50,60,70,80,90]
    reverse(scores)
    for score in scores:
        print(score,"",end="")
if __name__=="__main__":
    main()