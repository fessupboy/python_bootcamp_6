# def myfunc(a,b):
#     #Returns 5% of the sum of a and b
#     return sum((a,b)) * 0.05
# print(myfunc(40,60))

# def myfunc(*args):
# #     print(args)
# #     #return sum(args) *0.05
# #     for item in args:
# #         print(item)
# # print(myfunc(40,60,100,1,34))
# #
# #
# # def myfunc(**kwargs):
# #     print(kwargs)
# #     if 'fruit' in kwargs:
# #         print('My fruit of choice is {}'.format(kwargs['fruit']))
# #     else:
# #         print("I did not find any fruit here")
# # myfunc(fruit="apple",veggie='lettuce')

def myfunc(*args,**kwargs):
    print("I would like {} {}".format(args[1],kwargs['animal']))
myfunc(10,20,30,fruit="orange",food="eggs",animal="dog")