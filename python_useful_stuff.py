################################################
# Desription: A collection of useful patterns in python.
#     roughly sorted by topics.
# Author: Reik Schottstedt
# Date: 2022-12-27
# Summary: 
#
#
#
#
#
################################################


#################################################
# 100 helpful python tips
#################################################

# https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958


#################################################

# for-else condition for iterating through a list
numbers = [2, 4, 6, 8, 1]

for number in numbers:
    if number % 2 == 1:
        print(number)
        break
else:
    print("No odd numbers")

#################################################

my_list = [1, 2, 3, 4, 5]
one, two, three, four, five = my_list

#################################################

my_list = [1, 2, 3, 4]

print(my_list)  # [1, 2, 3, 4]

print(*my_list)  # 1 2 3 4

test = [*my_list]

def sum_of_elements(*arg):
    total = 0
    for i in arg:
        total += i

    return total


result = sum_of_elements(*[1, 2, 3, 4])
print(result)  # 10

#################################################

# list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)  # [2, 4, 6, 8]


#################################################

# dictionar comprehension
dictionary = {'first_element': 1, 'second_element': 2,
              'third_element': 3, 'fourth_element': 4}

odd_value_elements = {key: num for (key, num) in dictionary.items() if num % 2 == 1}

print(odd_value_elements)  # {'first_element': 1, 'third_element': 3}


#################################################

# true_expression if condition else false_expression
age = 30
age_group = "Adult" if age > 18 else "Child"
print(age_group)


#################################################

# list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

#################################################

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
squared_dict = {key + key: num * num for (key, num) in dict1.items() if num % 2 == 1 }
print(squared_dict)

#################################################

# find index i a list
books = ('Atomic habits', 'Ego is the enemy', 'Outliers', 'Mastery')

print(books.index('Mastery'))   # 3


#################################################

# named argumets
def subtract(a, b):
    return a - b


print((subtract(a=1, b=3)))  # -2
print((subtract(b=3, a=1)))  # -2

#################################################

# print seperator
print("Hello", end="")
print("World")  # HelloWorld
print("Hello", end=" ")
print("World")  # Hello World
print('words',   'with', 'commas', 'in', 'between', sep=', ')
# words, with, commas, in, between


#################################################

first_list = [1, 2, 3]
second_list = [1, 2, 3]

# Is their actual value the same?
print(first_list == second_list)  # True

# Are they pointing to the same object in memory
print(first_list is second_list)  
# False, since they have same values, but in different objects in memory


third_list = first_list

print(third_list is first_list)  
# True, since both point to the same object in memory


#################################################

# merge two dictionaries quickly
dictionary_one = {"a": 1, "b": 2}
dictionary_two = {"c": 3, "d": 4}

merged = {**dictionary_one, **dictionary_two}

print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#################################################

# Integers, floats, strings, booleans, and tuples are immutable
print(id(1))
print(id(2))
print(id("string"))
print(id(1))

name = "Fatos"
print(id(name))
name = "fatos"
print(id(name))

my_tuple = (1, 2, 3, 4)
print(id(my_tuple))

my_tuple = ('a', 'b')
print(id(my_tuple))

#################################################

# Lists, sets, and dictionaries are mutable
cities = ["Munich", "Zurich", "London"]
print(id(cities))  # 4482699712

cities.append("Berlin")
print(id(cities))  # 4482699712

#################################################

# Get the value of a character in Unicode
print(ord("A"))  # 65
print(ord("B"))  # 66
print(ord("C"))  # 66
print(ord("a"))  # 97

#################################################

# Get keys of a dictionary in a single line
dictionary = {"a": 1, "b": 2, "c": 3}
keys = dictionary.keys()
print(list(keys))  # ['a', 'b', 'c']

# Get values of a dictionary in a single line
dictionary = {"a": 1, "b": 2, "c": 3}

values = dictionary.values()

print(list(values))  # [1, 2, 3]

#################################################

# Swap keys and values of a dictionary

dictionary = {"a": 1, "b": 2, "c": 3}

reversed_dictionary = {j: i for i, j in dictionary.items()}

print(reversed)  # {1: 'a', 2: 'b', 3: 'c'}

#################################################



#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################


#################################################



#################################################



#################################################