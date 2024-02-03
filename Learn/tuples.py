#creat tuples
animal_tuple=("yellow anaconda","Reptile",30,5,20)
print(animal_tuple)

#create tuple from list
animal_tuple=tuple(["yellow anaconda","Reptile",30.5,20])
print(animal_tuple)

# indexing
#index value
first_index=animal_tuple.index("yellow anaconda")
print(first_index)

#value
third_item=animal_tuple[2]
print(third_item)

#slice tuples
sliced_tuple=animal_tuple[1:4]
print(sliced_tuple)

#modification
#tuples are immutable we can not change ,add or remove
#animal_tuple[0]="lion" -rais an error  #i tried to change the value to lion

# concatenation :-we can add elements to an existing tuple by appending another tuple to it.
animal_tuple_new=animal_tuple + ('swamp',False)

print(animal_tuple_new)


#Duplicates -it allow duplicates as they can be differentiated by their index
animal_tuple_new=animal_tuple_new+(False,)
print(animal_tuple_new)

# other methods
length_of_tuple=len(animal_tuple_new)
print(f'No. of attribute:{length_of_tuple}')

#count
count_false=animal_tuple_new.count(False)
print(count_false)

#tuple unpacking
animal_tuple =("yellow anaconda","Reptile",30.5,20)
name,group,av_weight,av_lifespan=animal_tuple
print(f"name:{name}")
print(f"group:{group}")








#source explore ai :data science academy-tuple course
