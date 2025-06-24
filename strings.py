print("# Strings:")
single_quoted = 'Hello'
double_quoted = "World"
multi_line = """This is a
multi-line string"""
print(len(single_quoted))

course = "Python Programming"
print(course[0])
print(course[-1])

text = "Python"

print(text[0])    # 'P' (first character)
print(text[-1])   # 'n' (last character)
print(text[1:4])  # 'yth' (from index 1 to 3)
print(text[::2])  # 'Pto' (every 2nd character)
print(text[0:])
print(text[:4])
print(text[:])
print("\n************************")
print("# Formatted Strings:")
greeting = "Hello" + " " + "World!"  # "Hello World!"
print(greeting)
first = "Priti"
last = "Kumari"
full = first + " " + last
print(full)

full = f"{first} {last}"
print(full)

full = f"{len(first)} {last}"
print(full)

name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")

print("\n************************")
print("# String Methods:")


subject = "python Programming"
print(subject.upper())
# subject_capital = subject.upper()
# print(subject_capital)
print(subject)
print(subject.lower())
print(subject.title())

print("\n************************")

course_name = "  Python Course   "
print(course_name.strip())   # removes the beginning and ending whitespaces
print(course_name.lstrip())  # removes the left whitespaces
print(course_name.rstrip())  # removes the right whitespaces
print("\n************************")
print(course_name.find("Pyth"))   # .find()	Returns first index of substring
print(course_name.find("pyth"))

print("\n************************")
print(course_name.replace("P", "J"))  # .replace()	Replaces substring

print("\n************************")
print("Python" in course_name)  # Check Substring (in keyword)
print("Java" not in course_name)
