"Como usar los dicts"

my_dict={
    'Daniel': 24,
    'Paula':20,
    'Rocío':55
    }

dict2 = my_dict.get('Paula','No encontre')
del my_dict['Paula']

for i in my_dict.values():
    print(i)
    
for i in my_dict.keys():
    print(i)
    
for i,j in my_dict.items():
    print(i,j)
    
a='Paula'in my_dict
b=24 in my_dict.values()
