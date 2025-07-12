# Example 1: Only if
age = 18

if age >= 18:
    print("You are an adult")  # Output: You are an adult

# Example 2: if ... else
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
# Output: You are not an adult

# Example 3: if ... elif ... else
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")
# Output: Grade: B

# Practice Example 1
weather = "raining"

if weather == "raining":
    print("Take an umbrella")

# Practice Example 2
hunger = True

if hunger:
    print("Eat food")
else:
    print("You're not hungry")
