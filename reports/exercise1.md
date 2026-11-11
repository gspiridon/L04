# Bug reports for exercise1.py

Line: 3  
Problem: The function `is_even(n)` incorrectly checks if a number is even by testing if `n % 2 == 1`, which returns true for odd numbers. For even numbers, the remainder when divided by 2 should be 0.  
Example: `is_even(4)` returns `False` (correct), but `is_even(3)` returns `True` (incorrect).  
Fix: Change the condition to `n % 2 == 0`.  
Corrected code:  
```python
def is_even(n):
    """true for even numbers"""
    return n % 2 == 0
```

Line: 8  
Problem: The `rectangle_area(width, height)` function incorrectly returns the sum of width and height instead of the product (area of a rectangle).  
Example: `rectangle_area(4, 5)` returns `9`, but the correct area should be `20`.  
Fix: Change the return statement to `width * height`.  
Corrected code:  
```python
def rectangle_area(width, height):
    """area of a rectangle."""
    return width * height
```

Line: 13  
Problem: The `double(n)` function incorrectly adds 2 to `n`, instead of multiplying it by 2.  
Example: `double(5)` returns `7`, but the correct result should be `10`.  
Fix: Change the return statement to `n * 2`.  
Corrected code:  
```python
def double(n):
    """twice the number n"""
    return n * 2
```
