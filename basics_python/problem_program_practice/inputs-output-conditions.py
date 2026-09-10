print("hello world")
name = "prajwal"
age = 22
print(name, age, sep="|", end="\n")
# name = input("Enter your name: ")
# print(name)
# age = int(input("Enter age: "))
# print(age)
# salary = float(input("Enter salary: "))
# print(salary)

# age = 22
# if age >= 18:
#     print("You are eligible to vote")

# age = 25
# has_license = True

# if age >= 18 and has_license:
#     print("Can drive")
# else:
#     print("Cannot drive")





age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")




role = "admin"

if role == "admin":
    print("Admin access")






# role = input("Enter role: ").lower()

# if role == "admin":
#     print("Full access")
# elif role == "manager":
#     print("Manager access")
# else:
#     print("Limited access")



name = "0"

if [6, 5, 7] == [5, 6, 7]:
    print("Name exists")
else:
    print("Name does not exist")



# print(bool(0))

#javascript ternery const result = age >= 18 ? "Adult" : "Minor";
#python ternery 
result = "Adult" if age >= 18 else "Minor"



# username = input("Username: ")
# password = input("Password: ")

# if username == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Invalid credentials")

user = {
    "name": "Prajwal",
    "role": "admin"
}
if user["role"] == "admin":
    print("Give admin access")

age = int("25")
print(age + 5)


name = ""
if name:
    print("Has name")
else:
    print("No name")




items = []

if items:
    print("Items available")
else:
    print("No items")



x = 10

if x > 5:
    print("A")

if x > 15:
    print("B")
else:
    print("C")


print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1]))


marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade F")
