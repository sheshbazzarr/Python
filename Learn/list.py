#create list
mammals=[]
print(mammals)
#create a list
mammals=["lion","elephant","dolphin"]

birds=list(("eagle","penguin","parrot"))
print(birds)
#range ()function
range_list=list(range(0,5,2))
print(range_list)

#print list print(birds) list type type(birds)
print(birds)
type(birds)

#copying a list
mammals_copy=mammals.copy()
print(mammals_copy)

# Nested lists
als_grouped=[mammals,birds]
print(als_grouped)


animals_grouped=[["lion","elephant","dolphin"],["eagle","penguin","parrot"]]
print(animals_grouped
      )

#indexing
first_index=birds.index("eagle")
print(first_index)

#accessing
second_item=birds[1]
print(second_item)

#slicing
animal_combined=["lion","elephant","Dolphin","eagle","penguin"]
sliced_list=animal_combined[2:5]
print(sliced_list)
