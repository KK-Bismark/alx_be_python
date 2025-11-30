# A division calculator that robustly handles errors like division by zero
# and non-numeric inputs from commandline arguments.


def safe_divide(numerator, denominator):
    try:
        try:
            result = float(numerator) / float(denominator)
        except ValueError:
            return "Error: please enter numeric values only."
    except ZeroDivisionError:
        return "Error: cannot divide by zero."
    else:
        return f"The result of the division is {result}"
