
#2
def new_format(string):
    format_string = ("{:,}".format(int(string)).replace(',', '.'))
    return format_string


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
print('Tests Done')

#1 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
# Additionally, if the number is negative, return 0.
#
# Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(number):
    sum = 0
    for i in range(2, number):
        if ((i % 3 == 0) or (i % 5 == 0)):
            sum += i
    return sum

#2 In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list
# with the strings filtered out.
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


def filter_list(l):
    l2 = []
    for i in l:
        if isinstance(i, int):
            l2.append(i)
    return l2

#3
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in
# descending order. Essentially, rearrange the digits to create the highest possible number.


def descending_order(num):
    num = str(num)
    list = []
    for nums in num:
        list.append(nums)
        list.sort()
    desc_str = ''.join(reversed(list))
    return int(desc_str)




#4
# Given an integral number, determine if it's a square number:
#
# In mathematics, a square number or perfect square is an integer that is the square of an integer;
# in other words, it is the product of some integer with itself.
#
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.


def is_square(n):
    if n>=0:
        if int(n**.5)**2 == n:
            return True
    return False

#5 ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly
# 6 digits.

# If the function is passed a valid PIN string, return true, else return false.
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false


def validate_pin(pin):
    lst = []
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if i.isdigit():
                lst.append(i)
    if len(lst) == 4 or len(lst) == 6:
        return True
    return False
