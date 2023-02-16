# # a=4
# # b=6
# # c=a+b
# # print(c)

# p=5000
# t=3
# r=2.5
# si=(p*t*r)/100
# print(si)

# a=12
# b=23
# c=a+b
# print(c)

# # Store input numbers
# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')

# # Add two numbers
# sum = float(num1) + float(num2)

# # Display the sum
# print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
# Python Program to find the area of triangle
float (a,b,c):

print("enter one side a= :")
print("enter one side b=: ")
print("enter one side c= :")
# a = 5
# b = 6
# c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
