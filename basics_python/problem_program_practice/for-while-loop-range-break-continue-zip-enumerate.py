

# for          → loop through items
# range()      → generate numbers
# while        → loop while condition is true
# break        → completely exit loop
# continue     → skip current iteration
# enumerate()  → index + value
# zip()        → combine multiple sequences
# nested loop  → loop inside loop



languages = ["Python", "Java", "C++"]
for language in languages:
    print(language)

#range(start, stop, step)
for i in range(5):
    print(i)
print("next question")
for i in range(1,5, 2):
    print(i)
print("next question")
for i in range(10, 0, -1):
    print(i)

print("next question")
for i in range(1, 11):
    if i == 5:
        break     #it will break the loop and exit the loop when i is equal to 5
    print(i)

print("next question")
for i in range(1, 11):
    if i == 5:
        continue       #it will skip the current iteration and move to the next iteration of the loop
    print(i)
print("next question")

name = "Prajwal"
for char in name:
    print(char)

print("next question")
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)

count = 1
print("next question")
while count <= 5:
    print(count)
    count += 1
print("next question")

print("this is using range and len for value and  index")
language = ["Python", "Java", "C++"]
for index in range(len(language)):
    print(index  ,language[index])

print("this is using enumerate for value and index")
for index, value in enumerate(language):
    print(index, value)

#zip 
print("this is using zip for value and index")
language = ["Python", "Java", "C++"]
framework = ["Django", "Spring", "React"]
version = [3.10, 17, 18]
for lang, frame ,ver in zip(language, framework, version,):
    print(lang, frame, ver)



#nested loops   
for i in range(3):
    for j in range(2):
        print(i, j)


print("next question")
for i in range(0, 10, 2):
    print(i)
print("next question")
for i in range(0, 10, 2):
    print(i)
print("next question")
for i in range(5):
    if i == 2:
        continue
    print(i)
print("next question")
count = 1

while count <= 3:
    print(count)
    count += 1

print("next question")
name = "Python"

for char in name:
    print(char)

print("next question")

numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)