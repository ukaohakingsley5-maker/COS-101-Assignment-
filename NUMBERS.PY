
from statistics import median, mode

# Function 1: Sum of numbers
def calculate_sum(numbers):
    return sum(numbers)


# Function 2: Average (Mean)
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Function 3: Median and Mode
def calculate_median_mode(numbers):
    if not numbers:
        return None, None

    med = median(numbers)

    try:
        mod = mode(numbers)
    except:
        mod = "No mode"

    return med, mod
