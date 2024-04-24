test_list = ['Apple','Banana','Blueberry','Strawberry','Kiwi','Orange']
print('Length of the list',len(test_list))
'''
print('First Item ', test_list[0])
middle_index = int(len(test_list)/2)
print('Middle Item',test_list[middle_index])
last_index = len(test_list)-1
print('Last Item',test_list[last_index])
'''

mixed_data_types = ['Tuhina',34,163.5,'Married','Greenford, London']
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print('List of IT Companies',len(it_companies))

print('First Item ', it_companies[0])
middle_index = int(len(it_companies)/2)
print('Middle Item',it_companies[middle_index])
last_index = len(it_companies)-1
print('Last Item',it_companies[last_index])
it_companies[3] = 'Netflix'
print(it_companies)
it_companies.append('Apple')
it_companies.insert(middle_index,'EY')
it_companies[2] = it_companies[2].upper()
print(it_companies)

#it_companies = '#;'.join(it_companies)
#print(it_companies)

'''
is_exists = 'Netflix' in it_companies
print(is_exists)
it_companies.sort()
print('Sorted order', it_companies)
it_companies.sort(reverse=True)
print('Reverse Order',it_companies)
first_three = it_companies[0:3]
print('First three companies',first_three)
last_three = it_companies[6:]
print('Last three companies',last_three)
middle_comp = it_companies[3:5]
print('Middle companies',middle_comp)

it_companies.pop(0)
print('Remove first item',it_companies)
it_companies.pop(4)
print('Remove middle item',it_companies)
it_companies.pop()
print('Remove last item',it_companies)

it_companies.clear()
print('Remove all items from the list',it_companies)

del it_companies
print('Delete it companines list',it_companies)
'''

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack.append('Python')
full_stack.append('SQL')
print('Join the list',full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('Sorting',ages)
median = (ages[3]+ages[4])/2
print('Median',median)
total = len(ages)
var1, var2, var3, var4, var5, var6, var7, var8, var9, var10 = ages
average = (var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10)/total
print('AVerage of the ages',average)
print('Ranges of age', ages[9]-ages[0])