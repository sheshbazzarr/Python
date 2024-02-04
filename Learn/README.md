#!/bin/python
tuples are immutable ,meaning we cannot change,add ,or remove items from a tupl once it has been created.
we would have to creat a new tuple with the desired changes.

lists allow duplicates : lists are mutable allows us to add ,remove,or modify elements in an existing list

add elements
append() this adds the element passed into it as a single element to the end of the list
insert()-- >insert an elements at specified postion
extend()--->this adds elements passed into it as separate elements to the end of the list


removing elemets
del() remove or delet an element at specific index
remove()--rist occurence of a specified value from the list
pop()---this remove and returns the element at the specified index


check membership
we can check for the prescence of an element in a list using the in keyword.
present ,True is returned

ordering list
sort()-->this sort the list in ascending order in place
if you want to sort the list in descending order ,we can specify the reverse paramaeter ture
sort(reverse=True)

sorted()--->new sorted list without modifying the original one.
 we can revers parammater -to order in descending order.

 Boolean methods:
 any()
 all()

 list methode
 len()-->determin how many elements a list has.


 count()--->to count the occurences of a particular element.

 source :explore ai 
