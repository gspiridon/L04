def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0

def is_adult(age):
    """Return True if age is 18 or older."""
    return age >= 18

def calculate_average(numbers):
    """Return the average or 0 for an empty list."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def remove_duplicates(items):
    """Remove duplicates while preserving the original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def binary_search(numbers, target):
    """Return the index of target in a sorted list, or -1."""
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1