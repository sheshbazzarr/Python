#creation of dictionary 
our_first_dictionary={}
our_first_dictionary['first_key']='first_value'
print(our_first_dictionary)


#creation of dict using dict()
our_first_dictinary=dict(first_key='first_value',extra_key='extra_value')
print(our_first_dictinary)

#create a nested dictionary
fynbos_familes={'erica':{'cape floristic region':670,'worldwide':4500},
                 'protea':{'cape floristic region':330,'worldwide':1350},
                 'restio':{'cape floristic region':273,'worldwide':1650},
                 'citrus':{'cape floristic region':135,'worldwide':900}
                 }

print(fynbos_familes)


#Accessing values in a nested dictionary 

print(fynbos_familes['erica'])

print(fynbos_familes['protea']['cape floristic region'])

protea_species=fynbos_familes['protea']
print(protea_species)


# extract keys
key_list=list(protea_species.keys())
print(key_list)

#extract values() method to extract a values object,which can also be converted to a list in order to access the elements.

value_list=list(protea_species.values())
print(value_list)
