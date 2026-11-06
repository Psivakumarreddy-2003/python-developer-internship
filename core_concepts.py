"""
YuvaIntern - Python Developer Fresher
Task 2: Core Concepts and Skills

Practice program covering variables, data types, operators, conditions,
loops, functions, lists, tuples, dictionaries, sets, and exception handling.
"""

def calculate_total(price, quantity):
    """Return the total cost for the given price and quantity."""
    return price * quantity


def get_grade(mark):
    """Return a grade based on a mark out of 100."""
    if not 0 <= mark <= 100:
        return "Invalid mark"
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    return "F"


def main():
    # 1. Variables and data types
    student_name = "Siva Kumar Reddy"  # str
    age = 21                            # int (example value for practice)
    average_mark = 82.5                 # float
    is_enrolled = True                  # bool

    print("=== Python Core Concepts ===")
    print("Student:", student_name)
    print("Age:", age)
    print("Average mark:", average_mark)
    print("Currently enrolled:", is_enrolled)

    # 2. Operators
    first_number = 15
    second_number = 4
    print("\n=== Operators ===")
    print("Addition:", first_number + second_number)
    print("Subtraction:", first_number - second_number)
    print("Multiplication:", first_number * second_number)
    print("Division:", first_number / second_number)
    print("Floor division:", first_number // second_number)
    print("Remainder:", first_number % second_number)

    # 3. Conditional statements
    print("\n=== Conditions ===")
    print("Grade for 82:", get_grade(82))

    # 4. Loops
    print("\n=== For loop: numbers 1 to 5 ===")
    for number in range(1, 6):
        print(number)

    print("\n=== While loop: countdown ===")
    count = 3
    while count > 0:
        print(count)
        count -= 1
    print("Go!")

    # 5. Collections
    subjects = ["Python", "Mathematics", "Database"]
    subject_tuple = ("Python", "Mathematics", "Database")
    student = {"name": student_name, "course": "Python", "mark": 82}
    unique_numbers = {1, 2, 2, 3, 3, 4}

    print("\n=== Collections ===")
    print("List:", subjects)
    print("Tuple:", subject_tuple)
    print("Dictionary:", student)
    print("Set (duplicates removed):", unique_numbers)

    # 6. Function and arithmetic
    print("\n=== Function ===")
    print("Total price:", calculate_total(250, 3))

    # 7. Exception handling
    print("\n=== Exception handling ===")
    try:
        result = 10 / 2
        print("10 / 2 =", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    finally:
        print("Calculation example completed.")


if __name__ == "__main__":
    main()
