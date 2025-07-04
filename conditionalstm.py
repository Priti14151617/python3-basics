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

print("*" * 50)
print("Logical Operators:")
high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

print("*" * 50)
print("Short-circuit Evaluations:")
high_salary = False
good_grade = True
employee = True
if high_salary and good_grade and not employee:
    print("Eligible")
else:
    print("Not Eligible")

print("*" * 50)
print("Chaining Comparison Operators:")
age = 22  # age should be between 18 and 55
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not Eligible")
