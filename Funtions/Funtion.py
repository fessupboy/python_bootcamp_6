# def name_of_function():
#     '''
#     DOCSTRING: Information about funtion
#     Input: no input
#     Output: Hello
#     '''
#     print("Hello")
# help(name_of_function)
# name_of_function()
#
#
# def add_funtion(num1,num2):
#     return num1+num2
# print(add_funtion(2,3))

#
# def say_hello(name = "NAME"):
#     return "Hello " +name
# result = say_hello()
# print(result)

#
# def add(n1,n2):
#     return n1+n2
# result = add(20,30)
# print(result)

# Find out if the word dog is in a string
# def dog_check(mystring):
# #     if 'dog' in mystring.lower():
# #         return True
# #     else:
# #         return False

# def dog_check(mystring):
#     return 'dog' in mystring.lower()
#
# print(dog_check("My Dog ran away"))
# print(dog_check("Cat ran away"))
# 'dog' in 'dog ran away'

#Pig latin
def pig_latin(word):
    first_letter = word[0]
    #check if vowel
    if first_letter in "aeiou":
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + first_letter + "ay"
    return pig_word
print(pig_latin('apple'))