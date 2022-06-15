 # BOOLEANS AND COMPARISONS
truthy = True
falsy = False

age = 20
is_over_age = age >= 18
is_under_age = age <= 18
is_twenty = age == 20

print(is_over_age,is_under_age,is_twenty)

my_number =5
user_number = int(input('Enter a number: '))

print(my_number == user_number)
print(my_number != user_number)

age = int(input('Enter your age: '))
age >= 18 and age <= 65

yes = True and True
no = True and False

print(no)

"""
'or' is used to get the second value if the first one is false. 
if the first one is true,
it gets the first value.
"""

which_one_is_it = True or False
second_one = False or True
first_one = True or True
neither = False or False

absolutely = not False #true
another_no = not True # false

is_programmer = True
is_learning = False

awesome = is_programmer and is_learning
less_awesome = is_programmer and is_learning

is_designer = False
