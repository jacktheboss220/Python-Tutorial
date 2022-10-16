# A
# Project File
# On
# Python Programming Lab
# Submitted In Partial Fulfillment of The Requirement for The Of degree Of
# Bachelor of Computer Applications

# Session: 2022-23
# Submitted by
# Mahesh Kumar
# 202010101130077

# Under Guidance
# of
# Er. Sanjay Kumar
# Department of Computer Science
# And
# Information Systems

# Shri Ramswaroop Memorial University
# Lucknow-Dewa Road, Barabanki, U.P


#-------------------------------------------------------------------------------------------------------------#
# INDEX
#-------------------------------------------------------------------------------------------------------------#
# S.No	Name of Experiment	                                                        Date	Sign
# 1.	Introduction to python programming and Environment setup of python.
# 2.	Implementation of	 basic syntax, variable types, and basic operators.
# 3.	Implementation of Decision-Making Statements.
# 4.	Implementation of Python-Loops statements.
# 5.	Implementation of Numbers and Strings.
# 6.	Implementation of Lists, Tuples.
# 7.	Implementation of Dictionary.
# 8.	Implementation of Functions.
# 9.	Implementation of I/O.
# 10.	Implementation of Graphics.


#-------------------------------------------------------------------------------------------------------------#
# 1.	Introduction to python programming and Environment setup of python.
#-------------------------------------------------------------------------------------------------------------#

# Standard Data Types

# The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

# Python has five standard data types −

# Numbers
# String
# List
# Tuple
# Dictionary


################
# Python Numbers
################

# Number data types store numeric values. Number objects are created when you assign a value to them.

var1 = 1
var2 = 10

################
# Python Strings
#################

# Strings in Python are identified as a contiguous set of characters represented in the quotation marks.

str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST")  # Prints concatenated string

# This will produce the following result −

# Hello World!
# H
# llo
# llo World!
# Hello World!Hello World!
# Hello World!TEST

###############
# Python Lists
##############

# Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]).

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)             # Prints complete list
print(list[0])          # Prints first element of the list
print(list[1:3])        # Prints elements starting from 2nd till 3rd
print(list[2:])         # Prints elements starting from 3rd element
print(tinylist * 2)     # Prints list two times
print(list + tinylist)  # Prints concatenated lists

# This produce the following result −

# ['abcd', 786, 2.23, 'john', 70.2]
# abcd
# [786, 2.23]
# [2.23, 'john', 70.2]
# [123, 'john', 123, 'john']
# ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']

###############
# Python Tuples
###############

# A tuple is another sequence data type that is similar to the list.

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)                # Prints the complete tuple
print(tuple[0])             # Prints first element of the tuple
print(tuple[1:3])           # Prints elements starting from 2nd till 3rd
print(tuple[2:])            # Prints elements starting from 3rd element
print(tinytuple * 2)        # Prints the contents of the tuple twice
print(tuple + tinytuple)    # Prints concatenated tuples

# This produce the following result −

# ('abcd', 786, 2.23, 'john', 70.2)
# abcd
# (786, 2.23)
# (2.23, 'john', 70.2)
# (123, 'john', 123, 'john')
# ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')

###################
# Python Dictionary
###################

# Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs.

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}


print(dict['one'])          # Prints value for 'one' key
print(dict[2])              # Prints value for 2 key
print(tinydict)             # Prints complete dictionary
print(tinydict.keys())      # Prints all the keys
print(tinydict.values())    # Prints all the values

# This produce the following result −

# This is one
# This is two
# {'dept': 'sales', 'code': 6734, 'name': 'john'}
# ['dept', 'code', 'name']
# ['sales', 6734, 'john']


#-------------------------------------------------------------------------------------------------------------#
# 2.	Implementation of	 basic syntax, variable types, and basic operators.
#-------------------------------------------------------------------------------------------------------------#

