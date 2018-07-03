#
#
# def print_something(my_name, your_name="Sanghyuk"):
#     print("Hello {0}, My name is {1}".format(your_name, my_name))
#
#
# # print_something("Sanghyuk", "Sangwon")
# # print_something("Sanghyuk")
#
#
# def asterisk_test(a, b, *args):
#     x, y, z = args
#     print(x)
#     print(y)
#     print(z)
#     return sum(args)
# print(asterisk_test(1,2,3,4,5))

#
# def kwargs_test_1(**kwargs):
#     print(kwargs)
#     print(kwargs['first'])
#     print(kwargs['second'])
#
# kwargs_test_1(first="hi", second="hello")
# # def kwargs_test_2(**kwargs):
# #     print(kwargs)
# #
#
# def kwargs_test_3(one, two, *args, **kwargs):
#     print(one+two)
#     print(args)
#     print(kwargs)
#
# kwargs_test_3(3,4,5,6,7,8,9, first=3, second=4, third=5)
#


a=0;
midterm_set=set([1,5,7,4,3,2,1,1,2,3])
print(midterm_set)

for i in midterm_set:
    a = a+i
print(a)
