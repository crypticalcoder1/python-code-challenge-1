# assessment_solutions.py

# Task 1: Function to add two numbers
def add_numbers(num1, num2):
    result = num1 + num2
    print("Sum of " + str(num1) + " and " + str(num2) + " is: " + str(result))
    return result

# Task 2: Function to check if a number is even
def is_even(number):
    result = number % 2 == 0
    print(f"{number} is even: {result}")
    return result

# Task 3: Function to reverse a string
def reverse_string(text):
    result = text[::-1]
    print(f"Reversed string of '{text}' is: '{result}'")
    return result

# Task 4: Function to count vowels in a string
def count_vowels(text):
    vowels = 'aeiou'
    count = sum(1 for char in text.lower() if char in vowels)
    print(f"Number of vowels in '{text}' is: {count}")
    return count

# Task 5: Function to calculate factorial of a number
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of {n} is: {factorial}")
    return factorial

# Task 6: Function to apply a decorator
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    return decorator_func(func)

# Task 7: Function to sort a list of tuples by age
def sort_by_age(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
    print(f"Sorted list by age: {sorted_list}")
    return sorted_list

# Task 8: Function to merge two dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    print(f"Merged dictionary: {merged_dict}")
    return merged_dict

# Task 9: Class to represent a Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Example usage to demonstrate function outputs
if __name__ == "__main__":
    add_numbers(3, 5)
    is_even(4)
    reverse_string("hello")
    count_vowels("Hello World")
    calculate_factorial(5)
    
    @apply_decorator
    def greet(name):
        print(f"Hello, {name}!")

    greet("Alice")

    list_of_tuples = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    sort_by_age(list_of_tuples)

    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merge_dicts(dict1, dict2)

    my_car = Car("BMW", "X5", 2023)
    my_car.display_info()
