import math
import numpy

#name = input("Enter Name:")
#print("hello, {}!".format(name))


#a = int(input("Enter 1st num:"))
#b = int(input("Enter 2nd num:"))
#c = int(input("Enter 3rd num:"))
#print("sum of a+b+c=", a+b+c)


# curnum = int(input("Enter number"))
# print("The next number for the number {} is {}". format(curnum, curnum-1))
# print("The previous number for the number {} is {}". format(curnum, curnum+1))


# s = float(input("Enter area of square"))
# side = float(math.sqrt(s))
# print("Side of rectangle is", side)

# a = float(input("Enter a:"))
# b = float(input("Enter b:"))
# c = float(input("Enter a:"))
# p = a + b + c
# p = p/2
# print("p=",p)
# s = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print("s={}m2".format(s))

# kredsum = float(input("Enter sum of loan:"))
# percent = float(input("Enter percents:"))
# totalsum = kredsum+kredsum/100*percent
#
# print("Total sum: {}, Overpay: {}".format(totalsum, totalsum-kredsum ))

# a = int(input("enter a:"))
# b = int(input("enter b:"))
# if str(a).isdigit() and str(b).isdigit():
#     print("a + b = ", a + b)
#     print("a - b = ", a - b)
#     print("a * b = ", a * b)
#     print("a / b = ", a / b)
# else:
#     print("a or b is not number")


# from numpy import random
#
# values = random.randint(0, 10)
# print("randint:",values)
# print("Random float number  ", random.uniform(0,10))

# a = float(input("Enter a:"))
# b = float(input("Enter b:"))
# if(a < b):
#     print("a < b , {}".format(a))
# else:
#     print("a > b , {}".format(b))


# def mySign(num):
#     if(num<0):
#         print("-1")
#     elif(num>0):
#         print("1")
#     elif(num==0):
#         print("0")
#
# num = float(input("enter num:"))
# mySign(num)




# import operator
#
# operators={
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv}
#
# a = input("enter a:")
# b = input("enter b:")
# op = input("enter operator:")
#
# result = operators[op](int(a),int(b))
# print("{}{}{}={}".format(a,op,b,result))


# print("Enter  a, b ,c")
# # a = float(input("a = "))
# # b = float(input("b = "))
# # c = float(input("c = "))
# #
# # discr = b ** 2 - 4 * a * c
# # print("discr D = %.2f" % discr)
# #
# # if discr > 0:
# #     x1 = (-b + math.sqrt(discr)) / (2 * a)
# #     x2 = (-b - math.sqrt(discr)) / (2 * a)
# #     print("x1 ={} \nx2 = {}" .format(x1, x2))
# # elif discr == 0:
# #     x = -b / (2 * a)
# #     print("x = {}".format(x))
# # else:
# #     print("no roots")

def isGlasn(letr):
    for l in glasn:
        if (l == letr):
            return True


glasn= ["а","о","у"]
isglasnF = False
letr = input("input letr:")
isglasnF=isGlasn(letr)
if(isglasnF):
    print("Глассная")
else:
    print("Не глассная")


