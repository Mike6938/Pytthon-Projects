#variables and numbers
a = 1
b = 2
c = 3

my_sum = a + b
sum_2 =  5 + 10
print (my_sum,sum_2)

"""
letters, numbers, and underscores
can't start with a number
"""


math_ops = 1 + 3 * 4 / 2 - 2
print (math_ops)

float_division = 12 /3
print (float_division)

interger_division = 12 // 3
print (interger_division)

divi_with_reminder = 12 // 5 #should be 2.4
print (divi_with_reminder)

reminder = 12 // 5 #2r2
print (reminder)

#string and string formatting
my_string = 'hello world1'
print (my_string)

quote_string = 'he said "you are amazing!" yesterday'
print (quote_string)

escaped_quotes = "he said \'you are amazing\'' yesterday"
print(escaped_quotes)

#----
name = 'jose'
greeting = 'hello,' + name
print(greeting)

another_greeting = f'hello, {name}'
print(another_greeting)


your_name = input('Enter your name: ')

print(f'hello, {your_name}')

age = input('Enter your age: ')
print(f'you have lived for {age * 12} months.')

age = input('Enter your age: ')
age_num = int(age)
print(f'You have lived for {age * 12} months')

age = int(input('enter your age: '))
print(f'You have lived for {age * 12} months')

age = int(input('enter your age: '))
months = age * 12
print(f'You have lived for {age * 12} months')

"""
calculate number of seconds instead
"""

age = int(input('Enter your age: '))
print(f'you have lived for {age * 364 * 24 * 3600} seconds')

