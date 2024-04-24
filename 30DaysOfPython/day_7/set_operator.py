'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print('Set of IT companies',it_companies)

it_comp_2 = {'TCS','Infy','Wipro','Cognizant'}
it_companies.update(it_comp_2)
print('List of IT companies',it_companies)
it_companies.remove('Wipro')
print('Remove',it_companies)
'''
'''
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print('A and B Union',C)
print('A intersection B',A.intersection(B))
print('A is subset',A.issubset(B))
print('A and B disjoint',A.isdisjoint(B))
print('Join a and b',A.union(B))
print('Join B and A',B.union(A))
print('Symmetric diff',A.symmetric_difference(B))
del A
del B
'''

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print('Length of set',len(age_set))
print('length of list',len(age))
print('COmpare length',len(age_set) >= len(age))