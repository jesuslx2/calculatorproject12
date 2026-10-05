def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return b subtracted from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def percentage_change(old: float, new: float) -> float:
    """Return the percentage change from old to new."""
    if old == 0:
        raise ValueError("The old value cannot be zero.")
    return ((new - old) / old) * 100


def compound_growth(initial: float, rate: float, years: int) -> float:
    """Return an amount after compound growth."""
    if years < 0:
        raise ValueError("Years cannot be negative.")
    return initial * (1 + rate) ** years


# Tests
assert add(2, 3) == 5
assert subtract(7, 10) == -3
assert multiply(-4, 2) == -8
assert divide(8, 4) == 2
assert add(0, 0) == 0
assert percentage_change(100, 150) == 50


# Start calculator
operation = input("Choose add, subtract, multiply, or divide: ").lower()
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if operation == "add":
    result = add(first_number, second_number)
elif operation == "subtract":
    result = subtract(first_number, second_number)
elif operation == "multiply":
    result = multiply(first_number, second_number)
elif operation == "divide":
    try:
        result = divide(first_number, second_number)
    except ValueError:
        print("You cannot divide by zero.")
        result = None
else:
    print("That operation does not exist.")
    result = None

if result is not None:
    print("Result:", result)



