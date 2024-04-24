empty_tuple =()
sister_name = ('Mom','Soma','Bonu','Kabli','Chunmun')
brother_name = ('Raja','Rana','Chandu','Leen','Piku')

siblings = sister_name + brother_name
print('Sublings Name',siblings)
print('Number of Siblings',len(siblings))
family_members = list(siblings)
family_members.append('Mother')
family_members.append('Father')
print('Family Members',family_members)

siblings = family_members[0:10]
parents = family_members[10:]
print('Unpack sibling',siblings)
print('Unpack parents',parents)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_product = ('Milk','Cheese','Curd','Paneer','Butter')
food_stuff_tp = fruits + vegetables + animal_product
print('Food Stuff', food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print('Food stuff list first 3 items',food_stuff_lt[0:3])
print('Food stuff last three',food_stuff_lt[11:len(food_stuff_lt)])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia if exists', 'Estonia'in nordic_countries)
print('Iceland if exists', 'Iceland'in nordic_countries)