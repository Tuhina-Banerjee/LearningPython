'''
number = [0,1,2,3,4,5,6,7,9,10]

for no in number:
    print('Print the numbers from 0 to 10',no)

count = 10
while count>0:
    print('Using while operator print',count)
    count = count - 1


for i in range(0,7):
    for j in range(0,i+1):
        print('# ')
    print('\r')

'''

tech = ['Python', 'Numpy','Pandas','Django', 'Flask']
for name in tech:
    print('Technology name ',name)

sum = 0
for i in range(1,100):
    sum+= i 
print('Total sum of numbers',sum)

sum_even = 0
sum_odd = 0
for i in range(0,100):
    if i%2 == 0:
        sum_even+= i
    elif i%2 != 0:
        sum_odd+= i
print('Sum of Even numbers',sum_even)
print('Sum of odd numbers',sum_odd) 

fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(fruits):
    print('Reversed list',fruit)