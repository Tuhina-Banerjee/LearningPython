dog = {}
dog = {'name':'Luna','color':'white','breed':'Pug','legs':4,'age':10}
print('Dog details',dog)

student = {'first_name':'Max','last_name':'Doe', 'gender':'Male', 'age':33, 'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Karlsrogatan 1',
        'zipcode':'	17065'
    }, 'country':'Sweden', 'city':'Stockholm'}
print('Length of student dictionary',len(student))

print('CHeck the data type of skills', type(student['skills']))
student['skills'].append('HTML')
student['skills'].append('CSS')

print('Student skills',student)

dict_keys = student.keys()
dict_values = student.values()
print('Dictionary keys as a list',dict_keys)
print('Dictionary values as a list',dict_values)

student_new = student.items()
print('Dict to tuples',student_new)

del student['skills']
print('Delete one item frm Dict',student)

del dog
print(dog)