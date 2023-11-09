def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function_call
def add_numbers(a, b):
    return a + b

@log_function_call
def multiply_numbers(a, b):
    return a * b

# Example usage
result1 = add_numbers(3, 5)
# Output: Calling function 'add_numbers' with arguments: (3, 5)
#         Result: 8

result2 = multiply_numbers(2, 4)
# Output: Calling function 'multiply_numbers' with arguments: (2, 4)
#         Result: 8