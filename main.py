# Python Practice Document
# A collection of basic Python concepts to practice with

# 1. Variables and Data Types
print("=== Variables and Data Types ===")
name = "Alice"
age = 30
height = 5.7
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")


# 2. String Operations
print("\n=== String Operations ===")
greeting = "Hello, Python!"
print(greeting.upper())
print(greeting.lower())
print(f"Length: {len(greeting)}")
print(f"First 5 characters: {greeting[:5]}")


# 3. Lists
print("\n=== Lists ===")
fruits = ["apple", "banana", "cherry", "date"]
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
fruits.append("elderberry")
print(f"After adding elderberry: {fruits}")
print(f"List length: {len(fruits)}")


# 4. Loops
print("\n=== Loops ===")
# For loop
print("For loop - counting to 5:")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# While loop
print("While loop - countdown from 3:")
count = 3
while count > 0:
    print(count, end=" ")
    count -= 1
print("\n")

# Looping through a list
print("Iterating through fruits:")
for fruit in fruits:
    print(f"- {fruit}")


# 5. Conditionals
print("\n=== Conditionals ===")
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# 6. Functions
print("\n=== Functions ===")

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def greet(name, greeting="Hello"):
    """Greet someone with a custom or default greeting."""
    return f"{greeting}, {name}!"

print(f"Add 10 + 5: {add(10, 5)}")
print(greet("World"))
print(greet("Python", "Hi"))


# 7. Dictionaries
print("\n=== Dictionaries ===")
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}
print(f"Person: {person}")
print(f"Name: {person['name']}")
person["age"] = 31
print(f"After birthday: {person}")


# 8. List Comprehension
print("\n=== List Comprehension ===")
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Even numbers: {evens}")


# 9. Simple Algorithm - Check if Prime
print("\n=== Simple Algorithm ===")

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

test_numbers = [2, 3, 4, 5, 10, 17]
print("Prime number check:")
for num in test_numbers:
    print(f"{num} is prime: {is_prime(num)}")


# 10. Try-Except (Error Handling)
print("\n=== Error Handling ===")
try:
    result = 10 / 2
    print(f"10 / 2 = {result}")
    result = 10 / 0  # This will cause an error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


print("\n=== End of Practice Document ===")