import math
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

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter a:"))
p = a + b + c
p = p/2
print("p=",p)
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("s={}m2".format(s))