# Bug reports for homework.py

Line: 4
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For even numbers, the remainder when divided by 2 should be 0, not 1. This causes the function to incorrectly return True for odd numbers and False for even numbers.
Example: is_even(4) returns False (correct), but is_even(3) returns True (incorrect).
Fix: return n % 2 == 0

Line: 9
Problem: The function `is_adult(age)` returns `True` if age is greater than 18, but adults are typically defined as 18 or older, meaning age >= 18. Using `>` excludes age 18, which is incorrect.
Example: is_adult(18) returns False, but 18 should be considered an adult.
Fix: return age >= 18

Line: 14
Problem: The function `calculate_average(numbers)` will raise a ZeroDivisionError when the input list is empty because `len(numbers)` becomes 0, and division by zero is undefined.
Example: calculate_average([]) raises ZeroDivisionError.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 19
Problem: The function `remove_duplicates(items)` uses `list(set(items))`, which removes duplicates but does not preserve the original order of elements. For example, if items = [1, 2, 2, 3], the result will be [1, 2, 3] but the original order of the first occurrence of each element is lost.
Example: remove_duplicates([1, 2, 2, 3]) returns [1, 2, 3], but the original order of 1, then 2, then 3 is not preserved in a way that maintains sequence.
Fix: use a list to track seen elements and preserve order: seen = set(); result = []; for item in items: if item not in seen: seen.add(item); result.append(item); return result

Line: 27
Problem: The binary search loop condition is `while left < right`, which fails when the list has only one element (left == right). In such cases, the loop never runs, and the function returns -1 even when the target might be present. Also, the loop may not terminate correctly for edge cases like when the target is at the end or beginning.
Example: binary_search([1], 1) returns -1, but the target is present at index 0.
Fix: change the loop condition to `while left <= right` and adjust the mid and bounds logic to properly handle all cases. Corrected version: while left <= right: mid = (left + right) // 2; if numbers[mid] == target: return mid; elif numbers[mid] < target: left = mid + 1; else: right = mid - 1; return -1
