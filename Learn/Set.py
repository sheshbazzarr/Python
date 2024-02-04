#creat a set
eats_plants={"Giraffe","elephant","bear","rabbit","fox"}
print(eats_plants)

eats_meat=set(["lion","tiger","bear","hawk","fox","lion"])

print(eats_meat)

#check membership in set
"lion" in eats_meat

#Duplicates ,since sets are unordered,they do not allow duplicates.
eats_meat={"lion","tiger","bear","hawk","fox","lion"}
print(eats_meat)
#adding element
eats_plants.add('cow')
print(eats_plants)
eats_meat.update({'leopard','cheetah'})
print(eats_meat)

eats_plants.remove('rabbit')
print(eats_plants)

eats_plants.discard('deer')

all_animals=eats_meat.union(eats_plants)
print(all_animals)
omnivores=eats_meat.intersection(eats_plants)
print(ominvores)

