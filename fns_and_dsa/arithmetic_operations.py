# A python program that has a function that performs basic arithmetic
# operations.

def perform_operation(num1, num2, operation):
    # checking to see which operation to use
    match operation:
        case "add":
            return (num1 + num2)
        case "subtract":
            return (num1 - num2)
        case "multiply":
            return (num1 * num2)
        case "divide":
            if num2 == 0:
                result = "The first number isn't divisible by 0"
                return (result)
            else:
                return (num1 / num2)
