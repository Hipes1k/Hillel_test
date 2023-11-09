# 1
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
#
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
#
# import re
#
# def to_camel_case(text):
#     lst = re.split(r'[-_]', text)
#     lst2 = []
#     for number, word in enumerate(lst):
#         if number == 0:
#             lst2.append(word)
#         else:
#             lst2.append(word.capitalize())
#     return ''.join(lst2)
# print(to_camel_case("the-stealth-warrior"))

# 2
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
#
# Don't forget the space after the closing parentheses!


# def create_phone_number(n):
#     lst = [str(x) for x in n]
#     all_other = ('(' + ''.join(lst[0:3]) + ')') + ' ' + ''.join(lst[3:6]) + '-' + ''.join(lst[6:])
#     return all_other
# (create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))