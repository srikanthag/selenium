'''1 Write a program to find the length of the string without using inbuilt function (len)'''

# def _len(iterable):
#     _count = 0
#     for item in iterable:
#         _count += 1
#     return _count
# print(_len('Hello'))

# s = 'srikanth'
# count = 0
# for iten in s:
#     count += 1
# print(count)

'''2. Write a program to reverse a string without using any inbuilt functions.'''
# def reverse(any_string):
#     temp = []
#     for i in range(len(any_string)-1, -1, -1):
#         temp.append(any_string[i])
#     return ''.join(temp)
#
# print(reverse('Hello world'))

# a = 'srikanth'
# for item in range(len(a)-1, -1, -1):
#     print(a[item], end='')

# for item in a[::-1]:
#     print(item)

'''3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".'''
# s = 'Hello world'
# s.replace('world', 'universe')

'''4. How to convert a string to a list and vice-versa.'''
# s = 'srikanth'
# e = list(s)
# print(e)
# w = ''.join(e)
# print(w)

# import re
# a = 'srikanth'
# e = re.findall(r'\w', a)
# print(e)
#
# b = ''.join(a)
# print(b)

'''5. Covert the string "Hello welcome to Python" to a comma separated string.'''
# s = "Hello welcome to Python"
# temp = s.split()
# print(temp)

#comma separated chars
# import re
# char = re.findall(r'\w', s)
# print(char)

# ','.join(temp)
# 'Hello,welcome,to,Python'

# s = "Hello welcome to Python"
# words = s.split()
# print(words, sep=',')

'''6. Write a program to print alternate characters in a string.'''
# s = 'hello world'
# print(s[::2])  # Using Slicing Syntax

'''7. Write a Program to print ascii values of the characters present in a string.'''
# s = 'sriLKanth'
# for c in s:
# 	print(ord(c))

'''8. Write program to convert upper case to lower case and vice-versa without using inbuilt method.'''
# s = 'SRIkanth'
# for item in s:
#     if 'a'<=item<='z':
#         print(chr(ord(item)-32))
#     elif 'A'<=item<='Z':
#         print(chr(ord(item)+32))

'''9. Write program to swap two numbers without using 3rd variable.'''
# >>> a = 10
# >>> b = 20
# >>>
# >>> b, a = a, b
# >>> a
# 20
# >>> b
# 10
# >>>

'''10. Write program to merge two different lists.'''
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# c = [*a, *b]
# print(c)
# >>> a = [1, 2, 3]
# >>> b = [4, 5, 6]
# >>> a + b
# [1, 2, 3, 4, 5, 6]
# # Using chain
# >>> from itertools import chain
# >>> s = chain(a, b)     # Returns an iterator
# >>> list(s)
# >>> [1, 2, 3, 4, 5, 6]

'''11. Write program to read a random line in a file. (ex. 50, 65, 78th line)'''
# from itertools import islice
# def read_random_line(lineno):
#     with open('Data/access-log.txt') as f:
#         line = islice(f, lineno, lineno+1)
#         return list(line)
#
# print(read_random_line(2))

'''Alternate Solution'''
# def read_random_line(lineno):
#     f = open('Data/sample.txt')
#     for index, line in enumerate(f, start=1):
#         if index == lineno:
#             return line
# print(read_random_line(10))

'''12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)'''
# from itertools import islice
# def read_n_lines(start_line, end_line):
#     with open('Data/access-log.txt') as f:
#         s = islice(f, start_line,end_line)
#         for line in s:
#             print(line)
#
# read_n_lines(10, 15)

'''Alternate Solution'''

# def read_n_lines(start_line, end_line):
#     with open('Data/access-log.txt') as enumerate(f, start=1):
#         if index in range(start_line, end_line):
#            print(line)
#
# read_n_lines(10, 15)

'''13 Program to print last "N" lines of a file.'''
# from itertools import islice
# def last_n_lines(n):
#     with open('sample.txt') as f:
#         for line in f:
#             line_count += 1
#         f.seek(0)
#         lines = islice(f, line_count - n, None)
#         return list(lines)

# from collections import deque
# def tail(n):
#     with open('sample.log') as f:
#         d = deque(f, n)  # only last 'n' lines will be loaded to the deque
#         return d
#

# last_10_lines = tail(10)  # returns last 10 lines of the file
# for line in last_10_lines:
#     print(line)

'''14. Write a program to check if the given string is Palindrome or not without using reversed method.'''
# def is_palindrome(iterable):
# 	rev_iter = iterable[::-1]
# 	if iterable == rev_iter:
# 		return True
# 	else:
# 		return False

# print(is_palindrome('racecar'))
# print(is_palindrome('malayalam'))
# print(is_palindrome('hello'))

'''alternate method'''
# a = 'srikanth'
# if a == a[::-1]:
#     print('yes')
# else:
#     print('no')

# a = "srikanth"
# b = a[::-1]
# if a == b:
# 	print("palindrome")
# else:
# 	print("not palindrome")

'''15 Write a program to search for a character in a given string and return the corresponding index.'''
# def search_character(string, key):
# 	for index, c, in enumerate(string):
# 		if c == key:
# 			print(f'Character {c} is at index {index}')

# search_character('hello world', 'w')
# search_character('hello world', 'd')

# a = 'srikanth'
# c = 'i'
# for index, item in enumerate(a):
#     if c == item:
#         print(f"{item} present in {index} position")

# a = "srikanth"
# b = "k"
# for index, item in enumerate(a):
#     if item == b:
#         print(item, index)

'''16 Write a program to get the below output'''
# sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
# from collections import defaultdict
# d = defaultdict(list)
# words = sentence.split()
# for word in words:
#    d[word[0]].append(word)
# print(d)

'''17 Write a to replace all the characters with - if the character occurs more than once in a string'''
# my_string = 'hellohai' # O/P should be '-e--o-ai'
# new_string = ['-' if my_string.count(c) > 1 else c for c in my_string]
# print(''.join(new_string))

'''18 write a decorator that returns only positive values of subtraction'''
# def positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return abs(result)
#     return wrapper
#
# @positive
# def sub(a, b):
#     return a - b
#
# print(sub(1, 5))

'''19 How to get the count of number of instances of a class that is being created.'''
# class Login:
#     login_count = 0  # Class Variable that keeps count of login counts
#
#     def __init__(self):
#         Login.login_count += 1
#
# u1 = Login()
# print(Login.login_count)
# #
# u2 = Login()
# print(Login.login_count)
#
# u3 = Login()
# print(Login.login_count)

'''20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and 
if the item is integer of float it should reverse it.'''
# def spam(items):
#     for item in items:
#         if isinstance(item, str):   # Check if the item is an instance of String
#             print(item)
#         else:
#             temp = str(item)    # Typecast Integer to String
#             print(temp[::-1])   # Reverse the String
#
# spam(['apple', 'yahoo', '1234', 100, 123.76, '26.23'])

'''21 Write a class named Simple and it should have iteration capability.'''
# class Simple:
#     def __init__(self, items):
#         self._items = items
#
#     def __iter__(self):
#         return iter(self._items)
#
# s = Simple([1, 2, 3, 4, 5])
# for item in s:
#     print(item)

'''22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a'''
# class MyDict:
#     def __init__(self, d):
#         self._dict = d
#
#     def __getitem__(self, item):
#         return self._dict[item]
#
# __getattr__ method is called only for missing attributes.(i.e. if you try to access an attribute which is not in instance dict)
#     def __getattr__(self, name):
#         return self._dict[name]
#
# d = MyDict({'a': 1, 'b': 2})
# print(d.a)
# print(d.b)
# print(d['a'])
# print(d['b'])

'''23 Write a python program to get the below output'''
# sentence = "Hi How are you"
# # o/p should be "iH woH era uoy"
#
# sentence = "Hi How are you"
# words = sentence.split()
#
# reversed_words = [word[::-1] for word in words]
# print(reversed_words)
#
# print(' '.join(reversed_words))

'''24 Write a python program to get the below output'''
# sentence = "Hi How are you"
# # # o/p should be "ouy era woH iH"
# #
# sentence = "Hi How are you"
# print(sentence[::-1])

'''25 Write a lambda function to add two numbers (a, b)'''
# add = lambda a, b: a + b
# print(add(1, 2))
# print(add(100, 300))

'''26 What is the output of the following'''
# a = [1, 2, 3]
# b = [4, 5, 6]
# print([a, b])   # List of Lists
# print((a, b))   # Tuple of Lists

'''27 How to remove duplicates from the list without using inbuilt functions'''
# items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# uniques = []
# for item in items:
# 	if item not in uniques:
# 		uniques.append(item)
# print(uniques)

'''28 Find the longest word in the sentence'''
# sentence = "Hello world. Welcome to Python"
# words = sentence.split()
# d = {word: len(word) for word in words}
# print(max(d.items(), key= lambda item: item[-1]))

#alternate solurion
# sentence = "hello world welcome to programming"
# words = sentence.split()
# max_len = 0
# max_word = ''
#
# for word in words:
#     if len(word) > max_len:
#         max_len = len(word)
#         max_word = word
# print(max_len, max_word)

#alternate solurion
# sentence = "hello world welcome to programming"
# print(max(sentence.split(), key=len))

'''29 write a program to reverse the values in the dictionary if the value is of type String'''
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# rev = { key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(rev)

'''30 write a program to get 1234'''
# t = ('1', '2', '3', '4')
# a = ''.join(t)   # Use join function
# print(a)

# #split
# b = ','.join(a)
# print([b])

'''31 How to get the elements that are in list b but not in list a'''
# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# set_a = set(a)      # Convert the list to set
# set_b = set(b)
# print(set_b.difference(set_a))

#alternate solution
# a = [1, 2, 3]
# b = [1, 2, 3, 4]

# for item in b:
#     if item not in a:
#         print(item)

'''32 A function takes variable number of positional arguments as input. How to check if the arguments that are 
passed are more than 5'''
# def spam(*args):
#     if len(args) > 5:
#         print('Length of arguments passed is greater than 5')
#     else:
#         print('Length Argument passed is less than 5')
#
# spam(1, 2, 3, 4, 5, 6, 7)
# spam(1, 2)

'''33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.'''
# Assume Below is the contents of the log file

# lines = """CRITICAL:Hello world
#
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical"""
#
# from collections import defaultdict
# _errors = defaultdict(int)
# for line in lines.split('\n'):  # Split the line based on newline character
#     # Split each line based on ":" to separate out error message part.
#     error_type, other = line.strip().split(':')
#     _errors[error_type] += 1
#
# print(defaultdict)

'''34 Write a function to reverse any iterable without using reverse function.'''
# a = [1, 2, 3, 4, 5]
# _reversed = []
# for i in range(len(a)-1, -1,-1):
# 	_reversed.append(a[i])
#
# print(_reversed)

# def rev(args):
#     for item in args[::-1]:
#         print(item)
# rev([1, 2, 3, 4, 5])

'''35 Write a function to print the below output.'''
# # func("TRACXN", 0)  # Should print RCN
# # func("TRACXN", 1)  # Should print TAX
#
# def func(string, flag):
# 	if flag:
# 		return string[0::2]
# 	return string[1::2]
#
# print(func('TRACXN', 0))
# print(func('TRACXN', 1))

'''36 Sum all the numbers in the below string.'''
import re
# s = "Sony12India567Pvt2ltd"
# total = 0.00
# r = re.findall(r'[\d]', s)  #regular expression
# print(r)
#
# for item in r:
#     total += int(item)
# print(total)

#alternate method
# for item in s:
#     if item.isdigit():
#         total += int(item)
# print(total)

'''37 Write a program to sum all the numbers in below string.'''
# import re
# s = "Sony12India567Pvt2ltd" # eg.12+567+2
# rr = re.findall(r'[\d]+', s)
# print(rr)       #['12', '567', '2']
#
# total = 0.00
# for item in rr:
#     total += int(item)
# print(total)

'''38 Print all the numbers in the below list'''
a = ['abc', '123', 'hello', '23']
# for item in a:
#     if item.isnumeric():
#        print(item)

'''39 Program to print the number of occurrences of characters in a String without using inbuilt functions.'''
# s = 'helloworld'
# from collections import defaultdict
# d = defaultdict(int)
# for c in s:
# 	d[c] +=1
# print(d)

#alternate method
# d = {}
# for item in s:
#     d[item] = s.count(item)
# print(d)

'''40 Program to print only the repeated characters and count of the same.'''
# s = 'helloworld'
# from collections import defaultdict
# d = defaultdict(int)
# for c in s:
# 	d[c] +=1
# for key, value in d.items():
#     if value > 1:
#         print(key, value)

#alternate method
# d = {ch: s.count(ch) for ch in s if s.count(ch) > 1}
# print(d)

'''41 Write a program to get alternate characters of a string in list format.'''
# s = 'hello world welcome to python'
# alternate_chrs = [c for c in s[::2]]
# print(alternate_chrs)

# s = 'helloworld'
# l = [item for item in s[::2]]
# print(l)

'''42 Write a program to get square of list of number's using lambda function .'''
# a = [1, 2, 3, 4, 5]
# squares = lambda number: number ** 2
# print(squares)      #return address
# for item in a:
#     print(squares(item), end=',')

# b = lambda item: item ** 2
# res = map(b, a)
# print(list(res))


#alternate method
# b = [squares(item) for item in a]
# print(b)

#alternate method
# for item in a:
#     print(item**2)

# a = [1, 2, 3, 4, 5]
# d = lambda num: num**2
# print(d)
# for item in a:
#     print(d(item))


'''43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.'''
# def is_anagram(str1, str2):
#     if str1.upper() == str2.upper():    # Return False if both words are same
#         return False
#     s_str1 = sorted(str1.upper())   # Convert to upper case and sort
#     s_str2 = sorted(str2.upper())
#     if s_str1 == s_str2:    # Return True if both the lists are same
#         return True
#     else:
#         return False
# print(is_anagram('ate', 'eat'))

#alternate method
# def ana(st1, st2):
#     a = sorted(st1)
#     b = sorted(st2)
#     if a == b:
#         return True
#     else:
#         return False
#
# print(ana('eat', 'tea'))

'''44 Write a program to iterate through list and build a new list, only if the items of the list has even number of characters.'''

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# a = [name for name in names if len(name) % 2 == 0]
# print(a)

'''45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even number of characters.'''

# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# a = { name: len(name) for name in names if len(name) % 2 == 0}
# print(a)

'''46 Write a program which squares the numbers in a list using map object'''
# Squares of numbers using map
# map is used to map a function with a iterable
# a = [1, 2, 3, 4, 5]
#
# def squares(item):
#     return item ** 2
#
# # Returns a map object, which happens to be an iterator.
# m = map(squares, a)
#
# # To get the squares of numbers, feed the map object to for loop
# for item in m:
#     print(item)
#
# # Mapping lambda function to map object
# m = map(lambda item: item ** 2, a)


# a = [1, 2, 3, 4, 5]
# b = lambda num: num ** 2
# res = map(b, a)
# print(list(res))

'''47 Count number of lines in a file without loading the file to the memory'''

# Counting number of lines in a file without loading the file to the memory
# with open('sample.txt') as f:
#     _count = 0
#     # Iterate over a file object and increment the _count
#     for line in f:
#         _count +=1
#
# print(f'No of Lines: {_count}')

'''48 Printing line and line no's'''
# with open('sample.txt') as f:
#     for line_no, line in enumerate(f, start=1):
#         print(line_no, line)

'''49 Write a Program to print the sum of entire list and sum of only internal list'''
# l = [[1,2,3],[4,5,6],[7,8,9]]
# # Add the contents of internal list. ([6, 15, 24])
# sum_internal = [sum(item) for item in l]
# sum_whole_list = sum(sum_internal)
# print(sum_internal)
# print(sum_whole_list)

'''50 Write a program to reverse the list as below'''
# words = ["hi", "hello", "python"]
# # o/p ['nohtyp', 'olleh', 'ih']
# words = words[::-1]
# words = [word[::-1] for word in words]
# print(words)    #['nohtyp', 'olleh', 'ih']

# words = ["hi", "hello", "python"]
# for word in words[::-1]:
# 	print(word[::-1], end=',')

'''51 Write a program to update the tuple'''
# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# # o/p (1, 2, 3, 4, 100, 200, 300)
# t = t1 + t2
# print(t)

'''52 Write a program to replace value present in nested dictionary.'''
# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# # Replace "nose" with "net"
# for key, value in d.items():
#     if isinstance(value, dict):
#         d[key]['n'] = "net"
# print(d)

'''53 Write a program to count the number of white spaces in a file.'''
# c = 'hi hello'
# import re
# white_spaces = 0
# with open('data/sample.txt') as f:
#     for line in f:
#         match = re.findall(r'\s', line)
#         if match:
#             white_spaces += len(match)
# print(white_spaces)

'''54 Grouping anagrams.'''
# from collections import defaultdict
# words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
# d = defaultdict(list)
# for word in words:
# 	s = ''.join(sorted(word))
# 	d[s].append(word)
#
# print(d)

'''55 What is the difference between defaultdict and normal dictionary.'''

"""
Defaultdict
-----------
1. When each key is encountered for the first time, it will not be there in the mapping.
2. So an entry is automatically created with default value (an empty list in case of defaultdict of list and zero in case of defaultdict int).
3. When keys are encountered again, the look-up proceeds normally as like a normal dictionary.
4. So, in defaultdict, creation of key, initialisation will happen simultaneously. 

Normal Dictionary
------------------
1. In case of normal dictionary, if the key does not exist, "KeyError" is raised. 
2. In order to work on the value, first the key needs to be created and initialised.
"""

'''56 Explain property decorator in python.'''

'''57 What is Mutable and Immutable datatypes.'''

"""
1. Mutable datatypes are objects whose value can be changed after creation. e.g. list, dict, set, user defined classes.
2. Immutable datatypes are objects whose value can not be changed after creating. e.g. int, float, bool, tuple, namedtuple
"""

'''58 Explain get() method in dictionaries.'''
"""
point =  {'a': 1, 'b': 2}
1. Values of dictionary can be accessed in two different ways. using square bracket syntax and the other one is using get() method.
2. When we try to access a key of a dictionary which does not exist using square bracket syntax (point['c']), "KeyError" exception is raised.
3. When we try to access a key of a dictionary which does not exist using get() method (point.get('c')), None is returned and no exception is raised.
4. We can pass a positional argument to get() method as custom message, so that get() method returns the custom message if the key does not exist.
           e.g. profile.get('c', 'Sorry the key does not exist')
"""

'''59 Write a list comprehension to get a list of even numbers from 1-50'''
# evens = [item for item in range(1, 51) if item % 2 == 0]
# print(evens)

'''60 Find the longest non-repeated substring in the below string'''
# s = "This is a Programming language and Programming is fun"
# ss = s.split()
# # make dictionary with word and its length pair for only those words which are not repeated.
# d = { word: len(word) for word in ss if s.count(word) == 1}
# print(d)
#
# # Sort the dictionary based on values and get the last item
# p = sorted(d.items(), key=lambda item: item[-1])[-1]
# print(p)

'''61 Write a program to find the duplicate elements in the list without using inbuilt functions'''
# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# unique_items = set(names)
# for item in unique_items:
#     _count = 0
#     for name in names:
#         if item == name:
#             _count += 1
#     if _count > 1:
#         print(item)

'''62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions'''
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

# # Get the unique elements present in the list
# unique_items = set(names)
# d = {}
#
# for item in unique_items:
#     _count = 0
#     for name in names:
#         if item == name:
#             _count += 1
#     d[item] = _count
# print(d)

'''63 Write a function to check if the number is Prime'''
# def is_prime(number):
#     return not any([number % 2 == 0 for i in range(2, number)])
# print(is_prime(5))
# print(is_prime(4))

#alternate method
# n = 12
# for i in range(2, n):
#     if n % i == 0:
#         print('no')
#         break
# else:
#     print('yes')

'''64 How to create a tuple using range function'''
# n = tuple(range(12))
# print(n)

'''65 Write a program to find the largest number in the list without using any inbuilt functions'''
# numbers = [10, 20, 30, 40, 50]
# largest = 0
# for item in numbers:
# 	if item > largest:
# 		largest = item
# print(largest)

'''66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.'''
# a = 1234
# b = str(a)
# print(b[-1])

'''function'''
# def get_last_digit(number):
#     temp = str(number)	# Typecast Integer to String
#     return int(temp[-1])	# Return the last digit
# print(get_last_digit(123))

'''67 Write a program to find most common words in a given list.'''
# words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under']
# from collections import Counter
# c = Counter(words)
# print(c)
# x = c.most_common()
# print(x)

'''68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the 
last n elements from the given sequence, as a list'''
# def tail_(iterable, n):
#     if not isinstance(n, int):
#         raise TypeError('Value of N should be Positive Integer')
#     if n <= 0:
#         return []
#     return list(iterable)[-n:]
#
# print(tail_([1,2,3,4,5,6,7], 2))

'''69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.'''
# def is_perfectsqr(num):
#     for i in range(num):
#         if i ** 2 == num:
#             return True
#     return False
# print(is_perfectsqr(25))

'''70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.'''
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d = {item:names.count(item) for item in names if names.count(item) > 1}
# print(d)

'''71 Write a program to count the number of occurrences of each word in a file.'''
# from collections import defaultdict
# d = defaultdict(int)
# with open (sample.text) as file:
#     for line in file:
#         words = file.split()
#         for word in words:
#             d[word] += 1
# print(d)

'''72 Write a program to count the number of occurrences of vowels in a file.'''
# from collections import defaultdict
# d = defaultdict(int)
# with open (sample.text) as f:
#     for line in f:
#         for c in f:
#             if c in 'aeiouAEIOU':
#                 d[c] += 1
# print(d)

'''73 Write a program to print all numeric values in a list'''
# items = ['apple', 1.2, 'google', '12.6', 26, '100']
# for num in items:
#     if isinstance(num, (int, float, complex)):
#         print(num)

'''74 Triangle Patterns'''
# Left Justified Triangle
# for i in range(1, 6):
#     print(f"{'*'*i:<5}")

# Left Justified Triangle
# for i in range(1, 6):
#     print(f"{'*'*i:<5}")

# Equilateral Triangle
# for i in range(1, 6):
#     print(f"{'* '*i:^10}")

# Equilateral Triangle
# for i in range(6, 0, -1):
#     print(f"{'* '*i:^12}")

# Inverted Triangles (Left Justified)
# for i in range(6, 0, -1):
#     print(f"{'*'*i:<6}")

# Inverted Triangles (Right Justified)
# for i in range(6, 0, -1):
#     print(f"{'*'*i:>12}")

# Number Pattern in triangle (Left Justified)
# pat = ''
# for i in range(1, 6):
#     pat += str(i)
#     print(f'{pat:<5}')

# Number Pattern in triangle (Right Justified)
# pat = ''
# for i in range(1, 6):
#     pat += str(i)
#     print(f'{pat:>5}')

# Number Pattern in triangle (Centre)
# pat = ''
# for i in range(1, 6):
#     pat = pat + ' '+ str(i)
#     print(f'{pat:^10}')

'''75 Write a program count the occurrence of a particular word in the file'''
# def occ(word):
#     count = 0
#     with open(sample.text) as file:
#         for line in file:
#             count += ss
#         return count
# print(occ(word))

'''76 Write a program to map a product to a company and build a dictionary with company and list of products pair'''
# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 'iOS', 'Google Drive', 'One Drive']
# # Pre-defined products for different companies
# apple_products = {'iPhone', 'Mac', 'iWatch'}
# google_products = {'Gmail', 'Maps', 'Google Drive'}
# msft_products = {'Windows', 'One Drive'}
#
# from collections import defaultdict
# d = defaultdict(list)
# for item in all_products:
#     if item in apple_products:
#         d['apple'].append(item)
#     elif item in google_products:
#         d['google'].append(item)
#     else:
#         d['microsoft'].append(item)
#
# print(d)

'''77 Write a program to rotate items of the list'''
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
#
# def rotate(iterable, n):
#     for item in range(n):
#         f = iterable.pop()
#         iterable.insert(0, f)
#         return iterable
# print(rotate(names, 1))
# print(rotate(names, 2))
# print(rotate(names, 3))

# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# n = 2
# for _ in range(n):
#     f = names.pop()
#     names.insert(0,f)
# print(names)

'''78 Write a program to rotate characters in a string'''
# def rotate_string(string, n):
#     string = list(string)
#     for _ in range(n):
#         f = string.pop()
#         string.insert(0, f)
#     return ''.join(string)
# print(rotate_string("helloworld", 1))
# print(rotate_string("helloworld", 2))
# print(rotate_string("helloworld", 3))

# a = 'srikanth'
# b = list(a)
# n = 2
# for _ in range(n):
#     f = b.pop()
#     b.insert(0,f)
# print(b)

'''79 Write a program to count the number of white spaces in a given string'''
# import re
# sentence = """Hello world welcome to Python Hi  How are you. Hi how are you"""
# spaces = re.findall(r'\s', sentence)
# print(len(spaces))

#alternate solution
# count = 0
# for item in sentence:
#     if item == ' ':
#         count += 1
# print(count)

'''80 Write a program to print only non-repeated characters in a string'''
# s = 'helloworld'
# r = [c for c in s if s.count(c) == 1]
# print(r)

'''81 What is the difference between a list and a tuple'''
# 1. The main difference between a list and a tuple is that list's are mutable and tuples are immutable.
# 2. Python over allocates memory for lists. The reason for over allocation of memory is to support append operation.
# Where as in tuples, memory is not over allocated, as tuples does not support append operation.
# (Since tuples are immutable, it does not support append operation).
# 3. Tuples are more memory efficient than lists. (because in tuples no extra memory is allocated. It is fixed).
# 4. Tuples are negligibly faster than lists.

'''82 Write a program to print all the consonants in a given string'''
# s = 'helloworld'
# consonants = [c for c in s if c not in 'aeiou']
# print(consonants)

# for item in s:
#     if item not in 'AEIOUaeiou':
#         print(item)

'''83 Write a program to count the number of commented (#) lines in a text file'''
# with open(sample.text) as f:
#     count = 0
#     for line in f:
#         if line.startswith('#'):
#             count += 1
# print(count)

'''84 Write a program to check if the year is leap year or not'''
# import calendar
# print(calendar.isleap(2012))
# print(calendar.isleap(2013))
# print(calendar.isleap(2016))

'''85 Liner Search'''
# a = list(range(20))
# def _search(iterable, key):
#       return any(item == key for item in iterable)
# print(_search(a, 17))
#
# print(_search(a, 21))

'''86 Difference between xrange and range'''
# python2- xrange
# python3- range
#
# 1. xrange does not stop, start and step attributes. But range object has start, stop and step attributes.
#   Python-3
#   r = range(0, 10)
#   r.start
#   r.stop
#   r.step
#
#   r = xrange(0, 10)
#   In Python-2 The above attributes are not supported.
#
# 2. range Object supports slicing! But xrange does not support slicing
#
# 3. range object has __contains__ method implemented. So it supports membership testing.
#    But xrange does not implement __contains__ method.
#    So Python will iterate over each and every item in the range xrange object until it finds a match.
#    (So if you are searching for a number in range is faster than xrange)
#
# 4. rang

'''87 Write a program to count no of capital letters in a string'''
# s = 'SReISDRRKannth'
# d = {}
# for item in s:
#     if item.isupper():
#         d[item] =s.count(item)
# print(d)

'''88 Write a program to get the below output'''
# for i in range(1, 5):
#     print('* '*1)
#     j = i + 1
#     print('* '*j)

'''89 Write a program to get the below output'''
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2]
# [3, 4]
# [5, 6]
# [7, 8]
# [9]

# for item in range(0, len(a), 2):
#     print(a[item:item+2])

'''90 Write a program to check if the elements in the second list is series of continuation of the items in the first list'''
# a = [10, 12, 14, 16, 18]
# b = [20, 22, 24, 26, 28]
#
# a = [0, 5, 10, 15]
# b = [20, 25, 30, 35, 40]
#
# x = [10, 20, 30, 40]
# y = [50, 40, 60, 70]
#
# def _series(iter1, iter2):
#       # Get the difference of the series
#     diff = a[1]-a[0]
#       # Combine both the lists
#     c = iter1 + iter2
#     return all([True if c[i] + diff == c[i+1] else False for i in range(0, len(c)-1)])
#
# print(_series(a, b))
# print(_series(x, y))

'''91 What is the difference between append() and extend() method in list'''

# 1. append() method appends one item at the end of the list.
# 2. extend() method appends all the items of the iterable to the end of the list.
# 3. Both append() and extend() method's mutates the existing list.

'''92 Write a program to find the first repeating character in a string'''
# s = 'helloworld'
# for c in s:
#     if s.count(c) > 1:
#         print(c)
#         break

'''93 Write a program to find the index of nth occurrence of a sub-string in a string'''
# sentence = "hello world welcome to python hello hi how are you hello there"
# import re
# def index_nth_occurance(sentence, pat, n):
#       matches = re.finditer(pat, sentence)
#       _count = 0
#       for match in matches:
#          _count +=1
#          if _count == n:
#             return f"Start Index: {match.start()}, End Index: {match.end()}"
#
# print(index_nth_occurance(sentence, 'hello', 3))
# print(index_nth_occurance(sentence, 'hello', 2))

'''94 Write a program to print prime numbers from 1 to 50'''
# for item in range(50):
#     if item > 1:
#         for i in range(2, item):
#             if item % i == 0:
#                 break
#         else:
#             print(item)

'''95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd numbers 
first and then even numbers in sorted order'''
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# evens = [item for item in a if item % 2 == 0]
# odds = [item for item in a if not item % 2 == 0]
# evens.sort()
# odds.sort()
# sorted_list = [*odds, *evens]
# print(sorted_list)

'''96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted list, odd numbers should 
be in ascending order and even numbers should be in descending order'''
# a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
# # o/p should be [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]
# evens = [item for item in a if item % 2 == 0]
# odds = [item for item in a if not item % 2 == 0]
# evens.sort(reverse=True)
# odds.sort()
# sorted_list = [*odds, *evens]
# print(sorted_list)

#or
# even = sorted(evens, reverse=True)
# odd = sorted(odds)
# # res = (*odd, *even)
# res = odd + even
# print(res)

'''97 Write a program to count the number of occurrences of non-special characters in a given string'''
# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
# from collections import defaultdict
# d = defaultdict(int)
# for c in s:
#     if c.isalnum():
#         d[c] += 1
# print(d)

'''98 Grouping Flowers and Animals in the below list'''
# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
#
# from collections import defaultdict
# d = defaultdict(list)
# for item in items:
#     _item, group = item.split('-')
#     d[group].append(_item)
# print(d)

'''99 Grouping files with same extensions'''
# files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# from collections import defaultdict
# d = defaultdict(list)
# for item in files:
#     _item, group = item.split('.')
#     d[group].append(_item)
# print(d)

'''100 Filter only those characters except digits'''
# s = '@hello12world34welcome!123'
# b = ''.join(s)
# for item in b:
#     if not item.isdigit():
#         print(item, end=',')

# import re
# c = re.findall(r'\D', s)
# print(c)

'''101 Count number of words in a sentence. ignore special characters.'''
# sentence = "Hi there! How are you:) How are you doing today!"
# import re
# words = re.findall(r'\w+', sentence)
# # print(words)
# d = {}
# for word in words:
#     d[word] = words.count(word)
# print(d)


'''102 Grouping even and odd numbers'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}
# from collections import defaultdict
# d = defaultdict(list)
# for num in numbers:
#     if num % 2 != 0:
#         d[1].append(num)
#     else:
#         d[0].append(num)
# print(d)

'''103 Find all max numbers from the below list'''
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# m = max(numbers)
# for item in numbers:
#     if item == m:
#         print(item)

'''104 Find all max length words from the below sentence'''
# sentence = "hello worlyyd hi apple you yahoo to you"
# max_len_word = max(sentence.split(), key=len)
# max_len_words = [word for word in sentence.split() if len(word) == len(max_len_word)]
# print(max_len_words)

#or
# d = sentence.split()
# dd = sorted(d, key=len)
# print(dd[-1])

'''105 Find the range from the following string'''
# sentence = '0-0, 4-8, 20-20, 43-45'
# Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]
# words = sentence.split(',')
# _range = []
# for word in words:
#     start, end = word.split('-')
#     for i in range(int(start), int(end) + 1):
#         _range.append(i)
# print(_range)

'''106 Can we override a static method in python?'''
# no
# class Parent:
#     @staticmethod
#     def demo():
#         print('Running demo in Parent')
#
# class Child(Parent):
#     @staticmethod
#     def demo():
#         print('Running demo in Child')
#
# # b = Parent()
# # print(b.demo())
# c = Child()
# print(c.demo())

'''107 Write a function which returns the sum of lengths of all the iterables'''
# def len_itb(*args):
#     total = 0
#     for item in args:
#         total += len(args)
#     return total
# print(len_itb([1,2],[3,4,5]))

#no of arguments
# def len_(*args):
#     return len(args)
# print(len_(['srss'], 's'))

'''108 Replace whitespaces with newline character in the below string'''
# import re
# sentence = "Hello world welcome to python"
# d = re.sub(r'\s', '\n', sentence)
# print(d)

'''109 Replace all vowels with "*"'''
# sentence = "hello world welcome to python"
# word = re.sub(r'[aeiou]','**', sentence)
# print(word)

'''110 Replace all occurances of "Java" with "Python" in a file'''
# with open (sample.text) as file:
#     for line in file:
#         nl = re.sub(r'java.txt', 'python.txt', line)
#         print(nl)

'''111 Maximum sum of 3 numbers and Minimum sum of 3 numbers'''
# numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
# s = sorted(numbers)
# min_num= sum(numbers[:3])
# max_num = sum(numbers[-3:])
# print(min_num)
# print(max_num)

'''112 Write a program to get the output as below'''
# s = "python@#$%pool"
# o/p should be ['PYTHON', 'POOL']
# import re
# e = re.findall(r'\w+', s)
# l = [item.upper() for item in e]
# print(l)

'''113 Write a program to print all the number which are ending with 5'''
# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
# import re
# for number in numbers:
#     e = re.findall(r'5$', number)
#     if e:
#         print(number)

'''114 Write a program to get the indexes of each item in the below list'''
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# from collections import defaultdict
# d = defaultdict(list)
# for index, item in enumerate(names):
#     d[item].append(index)
# print(d)

'''115 Write a program to print "Bangalore" 10 times without using "for" loop'''
# print("Bangalore \n" * 10)

'''116 Write a program to print all the words which starts with letter 'h' in the given string'''
# import re
# e = re.findall(r'\bh\w+', 'hi how are you')
# print(e)

'''117 Write a program to sum all even numbers in the given string'''
# sentence = 'hello 123 world 567 welcome to 9724 python'
# import re
# e = re.findall(r'\d', sentence)
# print(e)
# sum = 0
# for item in e:
#     if int(item) % 2 == 0:
#         sum += int(item)
# print(sum)

'''118 Write a program to add each number in word1 to number in word2'''
# import re
# word1 = 'hello 1 2 3 4 5'
# word2 = 'world 5 6 7 8 9'
# n1 = re.findall(r'\d', word1)
# n2 = re.findall(r'\d', word2)
# total = []
# for num1, num2 in zip(n1,n2):
#     total.append(int(num1)+int(num2))
# print(total)

'''119 Write a program to filter out even and odd numbers in the given string'''
# import re
# sentence = 'hello 123 world 456 welcome to python498675634'
# num = re.findall(r'\d', sentence)
# even = [ev for ev in num if int(ev) % 2 == 0]
# print(even)
# odd = [od for od in num if int(od) % 2 != 0]
# print(odd)

'''120 Write a program to print all the number which are starting with 8'''
# numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']
# import re
# for number in numbers:
#     num = re.findall(r'^8', number)
#     if num:
#         print(number)

'''121 Write a program to remove duplicates from the list without using set or empty list'''
# l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
# l2 = l1[::]
# for item in l2:
#     if l1.count(item) > 1:
#         l1.remove(item)
# print(l2)

'''122 Print all the missing numbers from 1 to 10 in the below list'''
# numbers = [1, 3, 6, 8, 10]
# for num in range(1,11):
#     if num not in numbers:
#         print(num)

'''123 Write a python program to get the below output'''
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# # o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
# # Convert x to str.
# result = [''.join((str(x), y)) for x in l1 for y in l2]
# print(result)

'''124 Write a python program to get the below output'''
# word = "AAAAaaccYYY"
# # o/p ['Y3', 'c2', 'A4', 'a2']
# # Get all the unique characters
# unique_letters = set(word)
# # build a list of character and its count pair
# count = [''.join((letter, str(word.count(letter)))) for letter in unique_letters ]
# print(count)

'''alternate solution'''
# word = "AAAAaaccYYY"
# unique_letters = set(word)
# for letter in unique_letters:
#     b = letter,str(word.count(letter))
#     print(''.join(b), end=',')

'''125 What is the output of the below function call'''
# class Demo:
#     def greet(self):
#         print("hello world")
#
#     def greet(self):
#         print("hello universe")
#
# d = Demo()
# print(d.greet())

'''126 In the list below, find all the number pairs which results in 10 either when added or subtracted'''
# a = [5,6,4,3,2,3,5,6,7,3]
# for item1 in a:
#     for item2 in a:
#         if item1 != item2:
#             if item1 + item2 == 10 or item1 - item2 == 10:
#                 print((item1, item2))

'''127 Write a decorator to prefix +91 to the original phone numbers'''
# numbers = [1234567890, 123456790, 1234567890]
# def outer(func):
#     def wrapper(*args, **kwargs):
#         # numbers = args
#         result = [ "+91-"+str(number) for number in numbers]
#         return func(result)
#     return wrapper()
#
# @outer
# def phone(numbers):
#     for number in numbers:
#         print(number)

'''128 Write a program to get the below output'''
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# # o/p should be ['b', 'd']
# keys = list(d.keys())
# list = [item for item in keys[1::2]]
# print(list)

'''129 Can we have multiple init methods in a class'''
# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
# p = Point(1, 2, 3)
# print(p.a)
# print(p.b)
# print(p.c)

# Since Python is dynamically typed language, it takes the latest __init__ method.

'''difference between import os and from os'''
# import module: import the whole library.
# from: imports a specific member or members of the library.

'''composite keys'''
'''dictionary have tuple as key'''
# holidays = {(26,1):'rday',(15,8):'iday'}
# print(holidays.values())
# print(holidays.keys())

'''1) WAP to count no of words  and occurance of  word in a text file'''
# with open(sample.txt) as file:
#     d = {}
#     for line in file:
#         sp = line.split()
#         for word in sp:
#             d[word] = sp.count(word)
# print(d)

'''2) Why  POM used'''
# Page Object Model, also known as POM, is a design pattern in Selenium that creates an object repository
# for storing all web elements. It is useful in reducing code duplication and improves test case maintenance.

'''4) extract value from dict'''
# d = {'a':1, 'b':2}
# print(d.values())
#or
# for key,value in d.items():
#     print(value)

'''5) decorators'''
# Decorator is a function it takes another function and add extra functionality without alter the main function
# when function is decorate using @deccorator function.
# when interpreter execute @decorator 2 major thing will happen
# outer function parameter func takes address of main function
# the main function will take address of wraper function

'''6) self and cls'''
# using the self keyword, we can access both the instance variables and the class attributes
# Using the cls keyword, we can only access the members of the class

'''difference between list and array'''
# list is a container object, i.e. each slot of the list points to smoother object. it holds the reference of other
# objects.
# But in case of arrays, the memory slot does not hold the reference of the other objects, but it holds the
# actual value.

'''9)  your frd sends a python file..  You don't have any pychram or vscode or any .. How you will execute python file'''
# you will execute the python script in command prompt
# using command python demo.py

'''What is the difference between.py and .pyc file'''
# .py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program

'''what are inbuilt data types?'''
# Numeric Types:	int , float , complex
# Sequence Types:	list , tuple , range
# Mapping Type:	dict
# Set Types:	set , frozenset

'''what is monkey patching?'''
# the process of calling a function with different name

'''what is inheritance?'''
# a class inherit the properties of another class

'''what is polymorphism?'''
# same function by name but different behavior
# class Polymarph:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
# pol = Polymarph([1,2],[3,4])
# print(pol.add())
#
# pol = Polymarph(3,4)
# print(pol.add())

'''What is encapsulation'''
# Encapsulation in Python is the process of wrapping up variables and methods into a single entity

'''pickling and unpickling'''
# ???Pickling??? is the process whereby a Python object hierarchy is converted into a byte stream, and ???unpickling???
# is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into
# an object hierarchy

'''collection  or container object'''
# Collections in Python are containers that are used to store collections of data
# example list, dict, set, tuple and Strings can be defined as sequential collections of characters

'''Iterables and sequences'''
# An iterable is anything you can loop over with a for loop in Python. Iterables can be looped over, and anything
# that can be looped over is an iterable.

# Sequences are iterables that have a specific set of features. They can be indexed starting from 0 and ending at
# one less than the length of the sequence, they have a length, and they can be sliced. Lists, tuples, strings

# Sets, dictionaries, files, and generators are all iterables but none of these things are sequences.

'''data structures'''
# The basic Python data structures in Python include list, set, tuples, and dictionary. Each of the data structures
# is unique in its own way. Data structures are ???containers??? that organize and group data according to type.

'''function annotation'''
# it is only type of hint but it does not enforce type check

'''difference between package & module'''
# A module is a file containing Python code.
# inbuilt modules
# math
# time
# statistics
# os

# packages
# A package is basically a directory with Python files and a file with the name __init__ . py.

'''Exception'''
# to handle unexpected termination of the program
# The try block lets you test a block of code for errors.
# The except block lets you handle the error specific exception block
# finally block execute after normal termination of try block

# a = 10
# b = 0
# try:
#     print(a / b)
#     print(l.append(10))
#
# except ZeroDivisionError:
#     print("In except block")
#
# print("hello")

# s = 'srikanth'
# try:
#     print(o)
#
# except NameError as msg:
#     print(NameError)
#     print(msg)
#
# except ZeroDivisionError:
#     print(ZeroDivisionError)
#
# finally:
#     print('close')


'''why do you used pass'''
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed

'''what are iterators in python'''
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# consist of the methods __iter__() and __next__()

'''what you mean by list comprehension in python'''
# List comprehension is basically creating lists based on existing iterables.

'''what is the difference between JSON and a dictionary?'''
# JSON is a serialization format. That is, JSON is a way of representing structured data in the form of a textual string
# A dictionary is a data structure. But they aren???t the same: dictionaries are for working with data in
# your program, and JSON is for storing it or sending it around between programs.

'''What are the python modules did you use in your project?'''
# time
# webdriver

'''What is abstract class?'''
# An abstract class can be considered as a blueprint for other classes.

'''What is property and why do we use that?'''
# Properties are special kind of attributes which have getter, setter and delete methods like __get__, __set__
# and __delete__ methods

'''Have you used any version control tool in your project?'''
# Git: Git is a free and open source distributed code management and Version control system.
# config: This command sets the author name and email address respectively to be used with your commits.
# git config ??? global user.name ???[name]???
# git config ??? global user.email ???[email address]???

# init: This command is used to start a new repository.
# git init [repository name]

# add: This command adds a file to the staging area.
# git add (file name)

# commit: This command records or snapshots the file permanently in the version history.
# git commit -m ???[ Type in the commit message]???

# remote: This command is used to connect your local repository to the remote server.
# git remote add origin https://github.com/srikanthag/TYSS.git

# push: This command sends the committed changes of master branch to your remote repository.
# git push -u origin master

# version
# git --version

# clone: This command is used to obtain a repository from an existing URL.
# git clone [url]

# status: This command lists all the files that have to be committed.
# git status

# git log: This command is used to list the version history for the current branch
# git log

# git pull: This command fetches and merges changes on the remote server to your working directory.
# git pull [Repository Link]

# merge: This command merges the specified branch???s history into the current branch.
# git merge [branch name]

# branch: This command lists all the local branches in the current repository.
# git branch <branch-name>

# Viewing branches
# git branch

# git checkout: This command creates a new branch and also switches to it.
# git checkout <name-of-your-branch>

# revert(undo)
# git revert

# reset
# git reset [file]

# delete: This command deletes the file from your working directory and stages the deletion.
# git rm [file]

# show: show current changes
# git show [commit]

''' Can you check the presence of a folder on your system through a program'''
# os.path.isdir() method in Python is used to check whether the specified path is an existing directory or not

'''Which are the libraries you used in python?'''
# Selenium

'''os modules'''
# The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents,
# changing and identifying the current directory, etc.
# cwd = os.getcwdu()
# c = os.mkdir('___python')
# c = os.chdir()
# r = os.rmdir('___python')
# e = os.listdir()
# r = os.path.getsize()
# r = os.path.exists()

'''What are the opps concept you used in your project and why they are important?'''
# class and inheritance concepts are used in my project along with these concepts decorators are also used

'''What is constructor?'''
# A constructor is a unique method used to create and initialize an object of a class.

'''Class method vs Static Method'''
'''static method'''
# The Python static method can call without creating an instance or object. Although staticmethod belongs to a class,
# you can call directly by its name. If you want a function that doesn???t need any class variables or instance variables
# to operate, then you can create it as a static method.
# class Employee:
#     def func_message(self):
#         print('hello world')
#
#     @staticmethod
#     def func_msg():
#         print('hello universe')
#
# c = Employee()
# print(Employee.func_msg())

'''classmethod'''
# A class method receives the class as an implicit first argument, just like an instance method receives the instance

# class Student:
#     school_name = 'ABC School'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def change_school(cls, school_name):
#         # class_name.class_variable
#         cls.school_name = school_name
#
#     # instance method
#     def show(self):
#         print(self.name, self.age, 'School:', Student.school_name)
#
# jessa = Student('Jessa', 20)
# jessa.show()
#
# # change school_name
# Student.change_school('XYZ School')
# jessa.show()

# A class method can access or modify the class state while a static method can???t access or modify it.

'''OOPS: Object-oriented programming (OOP) is a style of programming characterized by the identification of 
classes of objects closely linked with the methods (functions) with which they are associated. 
It also includes ideas of inheritance of attributes and methods.'''

''' Class: Class is a object constructor consist set of functions '''
# __init__ used to construct instance variable, and it will initialize the object
# self: it is a first parameter it holds the address of instance

# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
# c = Calculator(2,3)
# print(c.add())
# print(c.sub())

# class Bankaccount:
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount= amount
#
#     def deposit(self, cash):
#         self.amount += cash
#
#     def withdraw(self, cash):
#         self.amount -= cash
#
# b = Bankaccount('srikanth', 700)
# res1 = b.deposit(300)
# res= b.withdraw(200)
# print(b.__dict__)

'''overload constructor'''
# we can have multiple constructors in class but latest will take

# class Student:
#     def __init__(self, name1, class1):
#         self.name1 = name1
#         self.clas1 = class1
#
#     def __init__(self, name2, class2, age):
#         self.name2 = name2
#         self.clas2 = class2
#         self.age = age
#
# s = Student('srikanth', 10, 16)
# print(s.__dict__)

'''class decorator'''
# Class decorators should take class as an argument and modified that class

# def prices(cls):
#     print('attaching class attribute')
#     cls.apple = {"iphone": 900, "ipad": 2800, "imac": 4500}
#     return cls
#
# @prices
# class ShoppingCart:
#     def demo(self):
#         print(self.apple)

'''Inheritance: Inheritance enables us to define a class that takes all the functionality from a parent class 
and allows us to add more.'''
'''single level inheritance'''
# class Parent:
#     def __init__(self, value):
#         self.value = value
#
#     def google(self):
#         print("executing parent google")
#
#     def apple(self):
#         print("executing parent apple")

'''Completely Independent Method'''
# class Child1(Parent):
#     def yahoo(self):
#         print("executing yahoo child1")

'''Overriding Parent class Method'''
# class Child2(Parent):
#     def apple(self):
#         print("executing child2 apple")

'''Overriding Parent class Method but reusing the original method in Parent'''
# class Child3(Parent):
#     def apple(self):
#          print("executing child2 apple")
#          super().apple()    # super is used to acces parent class attributes
# c3 = Child3(100)
# print(c3.apple())

'''Adding a new Attribute'''
# class Child4(Parent):
#     def __init__(self, value, extra):
#         self.extra_value = extra
#         super().__init__(value)
#
# c4 = Child4(100, 'srikanth')
# print(c4.apple())

'''Multiple inheritance: class derived from more than one base class'''
# class Child5(Child1, Child2):
#     pass
# c5 = Child5(100)
# print(c5.yahoo())

'''Multi-level inheritance: derived class derived from another derived class '''
# class a:
#     def demo(self):
#         print("class a demo")
#
# class b(a):
#     def demo(self):
#         print("class b demo")
#         super().demo()
#
# class c(b):
#     def demo(self):
#         print("class c demo")
#         super().demo()

'''encapsulation'''
# It describes the idea of wrapping data and the methods that work on data within one unit. This puts
# restrictions on accessing variables and methods directly and can prevent the accidental modification of data

'''getter and setter in python'''
# getters are the methods which help access the private attributes or get the value of the private attributes
# and setters are the methods which help change or set the value of private attributes.

'''protected : _ can be overriddn in child class'''
# class Bankaccount:
#     _intrest = 4      # we can change it
#
#     def deposite(self, amount):
#         print('deposit amount:', amount)
#
#     def withdraw(self, withdraw):
#         print('deposit withdraw:', withdraw)
#
#     def roi(self):
#         print("ROI is:", self.__class__._intrest)
#
# class SBaccount(Bankaccount):
#     _intrest = 6.5
#
# s = SBaccount()
# p= s.roi()
# print(p)

'''private : __ can not be overridden in child class'''
# class Bankaccount:
#     __intrest = 4     # we can't change it
# #
#     def deposite(self, amount):
#         print('deposit ammount:', amount)
#
#     def withdraw(self, withdraw):
#         print('deposit withdraw:', withdraw)
# #
#     def roi(self):
#         print("ROI is:", self.__class__.__intrest)
# #
# class SBaccount(Bankaccount):
#     __intrest = 6.5
#
# s = SBaccount()
# p= s.roi()
# print(p)

'''febnocii number seris'''
# def febonocii(num):
#     a = 0
#     b = 1
#     i = 0
#     while i <= num:
#         print(a)
#         c = a + b
#         a = b
#         b = c
#         i += 1
# febonocii(3)

# waf that checks if the given number is fibonocii number or not
# def febonocii(num):
#     a = 0
#     b = 1
#     while a <= num:
#         c = a + b
#         a = b
#         b = c
#         if a == num:
#             print(num, 'is a febenocii number')
#             break
#     else:
#         print(num, 'not febenocii number')
# febonocii(10)

''' factorial number '''
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# print(fact(5))

'''errors in python'''
# AssertionError: Raised when the assert statement fails.
# AttributeError: Raised on the attribute assignment or reference fails.
# GeneratorExit: Raised when a generator's close() method is called.
# ImportError: Raised when the imported module is not found.
# IndexError: Raised when the index of a sequence is out of range.
# KeyError:	Raised when a key is not found in a dictionary.
# MemoryError: Raised when an operation runs out of memory.
# NameError: Raised when a variable is not found in the local or global scope.
# NotImplementedError: Raised by abstract methods.
# OSError: Raised when a system operation causes a system-related error.
# SyntaxError: Raised by the parser when a syntax error is encountered.
# IndentationError:	Raised when there is an incorrect indentation.
# TabError:	Raised when the indentation consists of inconsistent tabs and spaces.
# SystemError: Raised when the interpreter detects internal error.
# TypeError: Raised when a function or operation is applied to an object of an incorrect type.
# UnicodeError:	Raised when a Unicode-related encoding or decoding error occurs.
# ValueError: Raised when a function gets an argument of correct type but improper value.
# ZeroDivisionError: Raised when the second operand of a division or module operation is zero.

# 1. What is pylint.
# Pylint is a plugin or extension that checks for syntax errors.Also, it tries to enforce coding standards according to
# PEP8 style guide. It can give recommendations/suggestions/hints about types.
#
# 3. What is the difference between while loop and for loop.
# The body of while loop gets executed until some condition is True. Once the condition if False, the control comes out
# of the while loop.
#
# The body of for loop get executed for some fixed number of iterations.
#
# 4. What are magic methods?
# Magic methods are special methods which starts and ends with double underscores. It is internally called by python.
# e can customise the behaviour of an object or class using magic methods. They are also called as protocols.
#
# e.g. when you ask for the length of the list len(names) internally python will call _len_ method on list object.
#
# E.g. when you check for membership "apple" in names python internally triggers _contains_("apple")

'''prime number'''
# n = 10
# for item in range(2, n):
#     if n % item == 0:
#         print('not a prime number')
#         break
# else:
#     print('prime number')

#genarate seris of prime number
# for n in range(15):
#     if n > 1:
#         for item in range(2, n):
#             if n % item == 0:
#                 break
#         else:
#             print(n)









