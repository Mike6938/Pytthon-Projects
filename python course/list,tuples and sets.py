my_variable = "hello"
my_list_variable = ['hello', 'hi', 'nice to meet you']
my_tuple_variable = ('hello', 'hi', 'nice to meet you')
my_set_variable = {'hello', 'hi', 'nice to meet you'}

print(my_list_variable)
print(my_tuple_variable)
print(my_set_variable)

short_tupple_variable= ('hello',) #put a comma to ensure python recognises its a tuple.
another_short_tuple = 'hello', #also a tuple.

print(short_tupple_variable)
print(another_short_tuple)

# -----

print(my_list_variable[0]) #called a subscript
print(my_tuple_variable[0])
#print(my_set_variable[0]) cant index sets

my_list_variable.append('another string')
print(my_list_variable)

my_tuple_variable = my_tuple_variable + ('another string',)
print(my_tuple_variable)

#Cant add a duplicate
my_set_variable.add('hello')
print(my_set_variable)

my_set_variable.add('love')
print(my_set_variable)