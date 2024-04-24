'''
age = int(input('Enter your age'))
min_age = 18
diff_age = 18-age
if age>= 18:
    print('You are old enough to drive')
else:
    print('You are {} more years to learn drive'.format(diff_age))

your_age = int(input('Enter your age'))
my_age = int(input('Enter my age'))
diff = your_age-my_age
if diff == 1:
    print('1 year of difference')
elif diff == 0:
    print('Same age group')
else:
    print('{} years of differences'.format(diff))


number_a = int(input('Enter a number'))
number_b = int(input('Enter b number'))
if number_a > number_b:
    print('Number a is greater',number_a)
elif number_b > number_a:
    print('Number b is greater',number_b)
else:
    print('Both are equal')


your_score = int(input('Enter your score'))
if your_score > 80:
    print('Your grade is A')
elif (your_score >=70 or your_score == 79):
    print('Your grade is B')
elif (your_score >=60 or your_score == 69):
    print('Your grade is C')
elif (your_score >=50 or your_score == 59):
    print('Your grade is D')
elif (your_score >=0 or your_score == 49):
    print('Your grade is F')


autumn = ['September','October','November']
winter = ['December','January','February']
spring = ['March','April','May']
summer = ['June','July','August']

season = input('Enter the month')

if season in autumn:
    print('The season is Autumn')
elif season in winter:
    print('The season is Winter')
elif season in spring:
    print('The season is Spring')
elif season in summer:
    print('The season is Summer')


fruits = ['banana', 'orange', 'mango', 'lemon']
enter_fruit = input('Enter fruit name')

if enter_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(enter_fruit)
    print('New fruit added to the list',fruits)

'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    mid_index = int(len(person.get('skills'))/2)
    print('Middle skill ',person['skills'][mid_index])
if 'skills' in person:
    bool_skill =  'Python' in person['skills']
    print('Python exists',bool_skill)
if (person['is_married'] == True and person['country'] == 'Finland'):
    print('{} {} lives in {}. He is married'.format(person['first_name'],person['last_name'],person['country']))

person_skills = person['skills']
skill_dict_fe = ['Javascript','React']
skill_dict_be = ['Node','Python','MongoDB']
skill_dict_fs = ['React','Node','MongoDB']
if skill_dict_fe == person_skills:
    print('He is a frontend developer')
elif skill_dict_be == person_skills:
    print('He is a backend developer') 
elif skill_dict_fs == person_skills:
    print('He is a fullstack developer')
else:
    print('Unknown Title')

