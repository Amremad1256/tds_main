def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function_call
def greet(name):
    print(f"Hello, {name}!")

@log_function_call
def multiply_numbers(a, b):
    return a * b

greet("Alice")
# Output: Calling function 'greet' with arguments: ('Alice',), {}
#         Hello, Alice!

result = multiply_numbers(3, 4)
# Output: Calling function 'multiply_numbers' with arguments: (3, 4), {}
#         Result: 12