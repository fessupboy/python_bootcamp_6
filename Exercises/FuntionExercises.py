# def lesser_of_two_evens(a,b):
# #     if a%2==0 and b%2==0 :
# #         if a > b:
# #             return b
# #         elif a < b:
# #             return a
# #     else:
# #         if a > b:
# #             return a
# #         else:
# #             return b
# # print(lesser_of_two_evens(2,5))

# def animal_crackers(text):
# #     word = text.split()
# #     if word[0][0] == word[1][0]:
# #         return True
# #     else:
# #         return False
# #
# # print(animal_crackers("l alll"))

# def makes_twenty(n1,n2):
#     if n1 == 20 or n2 == 20:
#         return True
#     elif n1+n2 == 20:
#         return True
#     else:
#         return False
# print(makes_twenty(20,10))

# def old_macdonald(name):
#     newName = list(name)
#     print(newName)
#     newName[0] = newName[0].upper()
#     newName[3] = newName[3].upper()
#     name = ''.join(newName)
#     print(name)
# old_macdonald("macdonald")

# def master_yoda(text):
#     newWord = text.split()
#     newWord = newWord[::-1]
#     print(newWord)
#     text = " ".join(newWord)
#     print(text)
# master_yoda("We are ready")

# def almost_there(n):
#     #print(abs(n))
#     if n <= 0:
#         return False
#     if abs(100 - n) <= abs(10 or 200) - n <=10:
#         return True
#     else:
#         return False
# print(almost_there(211))

# def has_33(nums):
#     #print(len(nums))
#     for i in range(0, len(nums)-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False
# print(has_33([1, 3, 1, 3]))

# def paper_doll(text):
#     result = ""
#     for i in text:
#         i = i*3
#         result += i
#     return result
# print(paper_doll('Hello'))

# def blackjack(a,b,c):
#     sum = a+b+c
#     list = a,b,c
#     print(list)
#     if sum <= 21:
#         return sum
#     if sum >= 21 :
#         if 11 in list:
#             return sum - 10
#         else:
#             return "BUST"
# print(blackjack(9,9,11))

# def summer_69(arr):
#     #print(arr)
#     value = 0
#     flag = 0
#     for i in arr:
#         if flag == 0:
#             if i == 6:
#                 flag = 1
#             else:
#                 value += i
#                 #print(value)
#         if flag == 1:
#             if i== 9:
#                 flag =0
#     return value
# print(summer_69([2, 1, 6, 9, 11]))

# def spy_game(nums):
#     #print(nums)
#     counter = 0
#     flag1 = 0
#     flag2 = 0
#     flag3 = 0
#     for i in nums:
#         #print(i)
#         if flag1 == 0:
#             if i == 0:
#                 flag1 = 1
#                 #print(i)
#         elif flag2 == 0:
#             if i == 0:
#                 flag2 =1
#                 #print(i)
#         elif flag3 == 0:
#             if i == 7:
#                 flag3 =1
#                 #print(i)
#                 return True
#     return False
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

