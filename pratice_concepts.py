print("hello world")

# num1 = float(input("Enter the first number for addition: "))
# num2 = float(input("Enter the second number for addition: "))
# sum_result = num1 + num2
# print(f"sum: {num1} + {num2} = {sum_result}")

# Division
# num3 = float(input("Enter the dividend for division: "))
# num4 = float(input("Enter the divisor for division: "))
# if num4 == 0:
#     print("Error: Division by zero is not allowed.")
# else:
#     div_result = num3 / num4
#     print(f"Division: {num3} / {num4} = {div_result}")




# Input the base and height from the user
# base = float(input("Enter the length of the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# # Calculate the area of the triangle
# area = 0.5 * base * height
# # Display the result
# print(f"The area of the triangle is: {area}")

#swap two variables 
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("display the original value ")
# print(f"a is {a} and b is {b}")
# #swap operation 
# temp = a
# a = b 
# b = temp 
# #swap print
# print("display swaped value ")
# print(f"a is {a} and b is {b}")


#generate random num
# import random 
# print(f"Random number: {random.randint(1,100)}")


# #python to convert km to miles
# km = float(input("enter dis in km : "))
# conversion_factor = 0.621371 
# miles = km * conversion_factor  
# print(f"{km} kilometers is equal to {round(miles,2)} miles")




# celsius = float(input("Enter temperature in Celsius: "))
# # Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")


# import calendar
# year = int(input("enter year: "))
# month = int(input("Enter month: "))
# cal = calendar.month(year, month)
# print (cal)




#solve quadratic eqn
# import math

# # Input coefficients
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# #Calculate the discriminant
# discriminant = b**2 - 4*a*c

# # Check if the discriminant is positive, negative, or zero
# if discriminant > 0:
#     # Two real and distinct roots
#     root1 = (-b + math.sqrt(discriminant)) / (2*a)
#     root2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print(f"Root 1: {root1}")
#     print(f"Root 2: {root2}")
# elif discriminant == 0:
#     # One real root (repeated)
#     root = -b / (2*a)
#     print(f"Root: {root}")
# else:
#     # Complex roots
#     real_part = -b / (2*a)
#     imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
#     print(f"Root 1: {real_part} + {imaginary_part}i")
#     print(f"Root 2: {real_part} - {imaginary_part}i")


#swap two variables without temp 
# a = 5
# b = 6
# #swapping without temp 
# a, b = b, a
# print("After swapping: ")
# print("a = ", a)
# print("b = ",b)


# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")



# year = int(input("Enter a year: "))
# #​divided by 100 means century year (ending with 00)
# # century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# # not divided by 100 means not a century year
# # year divided by 4 is a leap year
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# # if not divided by both 400 (century year) and 4 (not century year)
# # year is not leap year
# else:
#     print("{0} is not a leap year".format(year))






# num = int(input("enter the input number: "))

# #set a flag variable
# flag = False

# if (num == 1):
#     print(f"{num} not a prime number")
# elif num > 1 :
#     #check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag  = True     #if factor is found, set flag to true 
#             #break out of loop 
#             break 
#     #check if flag is True 
# if flag:
#     print(f"{num}, is not a prime no")
# else:
#     print(f"{num}, is a prime number")


# #print all prime nos. which lies from 1 to 10
# lower = 1
# upper = 10
# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#     # all prime numbers are greater than 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)



#Write a Python Program to Find the Factorial of a Number.
# num = int(input("Enter the number: "))
# factorial = 1
# if num < 0:
#     print("factorial of negative number dosent exist")
# elif num == 0 :
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print(f"Factorial of {num} is {factorial} ")



#multiplication table
# num = int(input("Display multiplication table of : "))

# for i in range(1, 11):
#     print(f"{num} X {i} = { num * i}")




# #Write a Python Program to Print the Fibonacci sequence.
# nterms = int(input("how many terms? "))
# #first two terms
# n1, n2, = 0, 1
# count = 0
# #check if the number of terms is valid
# if nterms <= 0:
#     print("please enter the positive integer")
# #if there is only one term, return n1
# elif nterms == 1:
#     print("Fibonacci sequence upto", nterms, ":")
#     print(n1)
# #generate fibonacci sequence
# else:
#     print("Fibonacci sequence:")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         #update values
#         n1 = n2
#         n2 = nth
#         count += 1



# #Write a Python Program to Check Armstrong Number?
# num = int(input("Enter the number: "))
# #Calculate the number of digits in num 
# num_str = str(num)
# num_digits = len(num_str)

# #Initialize variables
# sum_of_powers = 0
# temp_num = num

# # calculate the sum of digits raised to power of num_digits 
# while temp_num > 0:
#     digit = temp_num % 10
#     sum_of_powers += digit ** num_digits
#     temp_num //= 10

# #Check if it's an Armstrong number
# if sum_of_powers == num:
#     print(f"{num} is an Amstrong number.")
# else:
#     print(f"{num} is not an Amstrong number.")


#Write a Python Program to Find Armstrong Number in an Interval.

# # Input the interval from the user
# lower = int(input("Enter the lower limit of the interval: "))
# upper = int(input("Enter the upper limit of the interval: "))

# for num in range(lower, upper+1):
#     order = len(str(num)) #find the number of digits in 'num'
#     temp_num = num 
#     sum = 0

#     while temp_num > 0 :
#         digit = temp_num % 10
#         sum += digit ** order
#         temp_num //= 10

#     #check if 'num' is an Armstrong number
#     if num == sum:
#         print(num)




#Write a Python Program to Find the Sum of Natural Numbers.
# limit = int(input("enter the limit: "))
# #Initialize the sum 
# sum = 0
# #use a for loop to calculate the sum of natural numbers
# for i in range(1, limit+1):
#     sum = sum + i
# print("The sum of natural numbers upto ", limit, "is:", sum)