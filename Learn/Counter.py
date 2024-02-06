from collections import Counter
my_list=['a','b','c','d','a','f','b']
counter=Counter(my_list)
print(counter)

#accessing counter
print(counter['a'])
print(counter.get('b'))


#update
counter.update(['a','b','b','c','a'])
print(counter)
print(list(counter.most_common(2)))
print(list(counter.elements()))
print(type(counter))