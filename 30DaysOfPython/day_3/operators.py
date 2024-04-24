my_age = 33
my_height = 163.5
dummy_complex = 4+4j

#base = input('Enter base of triangle')
#height = input('Enter height of triangle')
#area_of_triangle = 0.5 * float(int(base) * int(height))
#print('Area of triangle:',area_of_triangle)

'''
side_a = input('Enter side a')
side_b = input('Enter side b')
side_c = input('Enter side c')
perimeter_of_triangle = float(int(side_a)+int(side_b)+int(side_c))
print('Perimeter of the Triangle',perimeter_of_triangle)
'''

'''
length = input('Enter length of the rectangle')
width = input('Enter width of the rectangle')
area_of_rectangle = float(int(length)*int(width))
print('Area of the rectangle',area_of_rectangle)
perimeter_of_rect = 2*(int(length)+int(width))
print('Perimeter of rectangle', perimeter_of_rect)
'''

'''
radius = input('Enter radius of the circle')
pi=3.14
area_of_circle = float(pi*(int(radius) ** 2))
print('Area of circle',area_of_circle)
circum_of_circle = float(2 * pi * int(radius))
print('Circumference of circle',circum_of_circle)
'''

'''
x = input('Enter value of x')
y = (2 * int(x)) - 2 
print('Value of first slope',y)

x1 = 2
x2 = 6
y1 = 2
y2 = 10

slope = (y2-y1)/(x2-x1)
print('Value of second slope',slope)

print('Compare the slope', slope!=y)


print(len('python')>len('dragon'))
print('on' in ('python' and 'dragon'))
print('jargon' in 'I hope this course is not full of jargon')
print(not('on' in ('python' and 'dragon')))
abc = float(len('python'))
print(abc)
xyz = str(abc)
print(type(xyz))


print('Comparison',(7 // 3) == int(2.7))
print('Type comparison',type('10') == type(10))

abc = int(float('9.8'))
print('Type comparison 2', abc == 10)


total_hours = int(input('Enter hours'))
rate_per_hr = int(input('Enter rate per hour'))
total_pay = rate_per_hr * total_hours
print('Total pay of the person',total_pay)
'''

one_year = 365 * 24 * 3600
no_of_year =  int(input('Number of years'))
total_secs = one_year * no_of_year
print('Number of sec a person lives', total_secs)