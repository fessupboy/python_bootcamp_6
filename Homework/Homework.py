# def vol(rad):
#     answer = 4/3 * 3.14 * rad**3
#     print(answer)
# vol(2)
#
# def ran_check(num,low,high):
#     if num >= low and num <= high:
#         print(f"{num} is in the range between {low} and {high} ")
#     else:
#         print(f"{num} is not in the range between {low} and {high} ")
# ran_check(8,2,7)
#
# def ran_bool(num,low,high):
#     if num >= low and num <= high:
#         return True
#     else:
#         return False
# print(ran_bool(3,1,10))

# def up_low(s):
#     ups = 0
#     lows = 0
#     for letter in s:
#         #print(letter)
#         if letter.isupper():
#             ups = ups+1
#         elif letter.islower():
#             lows = lows+1
#     print(f"Original String :  {s}")
#     print(f"No. of Upper case characters :  {ups}")
#     print(f"No. of Lower case Characters : {lows}")
#
# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)

# def unique_list(unique_list):
#     new_list = []
#     for num in unique_list:
#         #print(num)
#         if num not in new_list:
#             new_list.append(num)
#     print(new_list)
#
# unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# def multiply(numbers):
#     mult=1
#     for num in numbers:
#         #print(num)
#         mult = mult*num
#         print(mult)
# multiply([1,2,3,-4])

# def palindrome(s):
#     if s.replace(" ","") == s[::-1].replace(" ",""):
#         print(s)
#         print(s[::-1])
#         return True
#     else:
#         print(s)
#         print(s[::-1])
#         return False
#
# print(palindrome('nurses run'))

import string

# def ispangram(str1, alphabet=string.ascii_lowercase):
#     #print(alphabet)
#     for letter in alphabet:
#         #print(word)
#         for word in str1:
#             if word == letter:
#                 print(word)
#                 alphabet = alphabet.replace(word,"")
#                 print(alphabet)
#     print(alphabet)
#     if len(alphabet) == 0:
#         print(len(alphabet))
#         return True
#     else:
#         return False
#

