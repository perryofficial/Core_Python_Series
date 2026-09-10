#creating a string
name = "Prajwal"
name = 'Prajwal'
text = f"Hello {name}"
print(text)
#string indexing
print(name[0])
#string negative indexing
print(name[-1])
#string slicing    string[start:end]
print(name[0:4])
#omitting start index
print(name[:2])
#omitting end index
print(name[2:])
#Copying the Entire String
print(name[:])
#Step in Slicing
print(name[0:7:2])
#reversing a string
print(name[::-1])
#strings are immutable
name = "Prajwal"
#name[0] = "P" this will give an error because strings are immutable
name = "X" + name[1:]
print(name)
#len()function
name = "Prajwal"
print(len(name))
#upper() and lower() methods
print(name.upper())
print(name.lower())
#strip() method
name = "   dostana   "
print(name.strip())
#replace() method
text = "Hello dostana kya baat hai bro"
text = text.replace("dostana", "Prajwal")
print(text)
#split() method
text = "Hello dostana kya baat hai bro"
text = text.split(" ")
print(text) 
#join() method
text = ["Python", "is", "awesome", "and", "super", "easy"]
text = " ".join(text)
print(text)
print(type(text))
#find method
text = "Hello dostana kya baat hai bro"
print(text.find("dostana"))
#startswith() and endswith() methods
text = "Hello dostana kya baat hai bro"
print(text.startswith("Hello"))
print(text.endswith("bro"))
#f-strings 
topic = "Python"
level = "beginner"
prompt = f"""
Explain {topic} to a {level} developer.
Give practical examples.
"""
#print(prompt)

#string checking methods
text = " 123"

print(f"text.isalpha(): {text.isalpha()}")
print(f"text.isdigit(): {text.isdigit()}")
print(f"text.isalnum(): {text.isalnum()}")
print(f"text.isspace(): {text.isspace()}")

text = "  Hello Python  "
words = text.split()
len(text)                 # length
text.upper()              # uppercase
text.lower()              # lowercase
text.strip()              # remove outer whitespace
text.replace("a", "b")    # replace
text.split()              # string → list
" ".join(words)           # list → string
text.find("Python")       # find position
text.startswith("Hello")  # prefix check
text.endswith("Python")   # suffix check


text[0]       # first character
text[-1]      # last character
text[:3]      # first 3 characters
text[3:]      # from index 3
text[::-1]    # reverse


