# x =25
#
# def printer():
#     x = 50
#     return x
# print(x)
#
# print(printer())


#GLOBAL
# name = "THIS IS A GLOBAL STRING"
# def greet():
#     #ENCLOSING
#     name = 'SAMMY'
#
#     def hello():
#         #LOCAL
#         name = "I'M A LOCAL"
#         print("HELLO " +name)
#     hello()
# greet()


x = 50
def func(x):
    #global x
    print(f"X is {x}")

    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    x = "NEW VALUE"
    print(f"I JUST LOCALLY CHANGED X TO {x}")
    return x
print(x)
x = func(x)
print(x)