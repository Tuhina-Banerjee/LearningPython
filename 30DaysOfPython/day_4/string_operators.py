first_str = 'Thirty'
sec_str = 'Days'
third_str = 'Of'
four_str = 'Python'

final_str = '30DaysOfPython'
#print(final_str,len(final_str))
#print(final_str.swapcase())
#print(final_str[6:])
#print(final_str.find('Thirty'))
#print(final_str.replace('Python', 'Coding'))
#print(final_str.split())
demo_str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(demo_str.split(','))
print(final_str[0])
last_ind = (len(final_str))-1
test_str = 'You cannot end a sentence with because because because is a conjunction'
sub_str = 'because'
print(test_str.index(sub_str))
print(test_str.rfind('because'))
print(test_str[31:54])
print(final_str.isidentifier())
python_library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
final = '# '.join(python_library)
print(final)

new_str = 'Name\t\tAge\tCountry\t\tCity \nAsabeneh\t250\tFinland\t\tHelsinki'
print(new_str)

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))