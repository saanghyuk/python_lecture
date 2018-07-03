# user_input_number="234"
# random_number="342"
#
# strikes=0
# balls=0
# user_input_list  = list(user_input_number)
# random_number_list = list(random_number)
#
# len(random_number_list)
# for i in range(0,len(user_input_list)):
#     if(user_input_list.count(random_number_list[i])==1):
#         if(user_input_list[i]==random_number_list[i]):
#             strikes+=1
#         else:
#             balls+=1
#
#
# # print(strikes_or_ball)
#
#
# strikes_or_ball = [strikes,balls]
# print(strikes_or_ball)

#
#
#
# a=["1", "2", "3"]
# print(a.count("3")
result=""
one_more_input="123"
if(one_more_input.lower()=="y" or one_more_input.lower()=="yes" ):
    result=True
else:
    result=False
print(result)





# #
# # three_digit="222"
# # result=""
# # check=""
# # initial_set = set(three_digit)
# #
# # set_to_list= list(initial_set)
# #
# # for i in range(0, len(set_to_list)):
# #     check+=set_to_list[i]
# #
# # if(sorted(check)==sorted(three_digit)):
# #     result= False
# # else:
# #     result = True
# #
# # print(result)
#
# import random
# def get_random_number():
#     # Helper Function - 지우지 말 것
#     # 100부터 999까지 수를 램덤하게 반환함
#     return random.randrange(100, 1000)
#
# result=0;
# check_duplicated = True;
# rand_number=0;
# while check_duplicated:
#     rand_number=get_random_number()
#     str_number = str(rand_number)
#     listed_number =list(str_number)
#     seted_number= set(listed_number)
#     sorted_list = sorted(listed_number)
#     sorted_set = sorted(seted_number)
#     if(sorted_list==sorted_set):
#         check_duplicated =False
#         result=rand_number
#     else:
#         check_duplicated=True
# print(result)
# str_number = str(get_random_number())
# print(str_number)
# listed_number =list(str_number)
# seted_number= set(listed_number)
#
# sorted_list = sorted(listed_number)
# sorted_set = sorted(seted_number)
#
# if(sorted_list==sorted_set):
#     print(True)
# else:
#     print(False)
