import sys 
def shell_sort(array):
    length=len(array)
    gap=int(length/2)
    while gap>0:
        for i in range(gap,length):
            j=i
            while(j-gap)>=0 and array[j]<array[j-gap]:
                swap(array,j,j-gap)
                j=j-gap


            gap=int(gap/2)
def swap(array,a,b):
    array[a]=array[a]+array[b]
    array[b]=array[a]-array[b]
    array[a]=array[a]-array[b]
def main():
  
    scores = [ 9 , 6 , 5 , 8 , 0 , 7 , 4 , 3 , 1 , 2 ]
    shell_sort( scores)
    length = len( scores)
    for i in range( 0 , length):
        print ( scores[ i] ,   " , " , end= "" )
if __name__ == "__main__" :
    main()

