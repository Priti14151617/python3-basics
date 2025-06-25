print("1. if statement:")
age = 18
if age >= 18:
    print("You are an adult")
print("*" * 50)
print("2. if-else statement:")
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")
print("*" * 50)
print("3. if-elif-else statement:")
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print(f"Your grade is {grade}")
print("*" * 50)
print("4. Nested conditionals:")
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Number is not positive")
print("*" * 50)
print("5. Ternary operator (conditional expression):")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
