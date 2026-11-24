import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_is_even():
    """Test that is_even returns True for even numbers and False for odd numbers."""
    assert is_even(4) == True  # 4 is even, should return True


# bug report 2
def test_r2_is_adult():
    """Test that is_adult returns True for age 18, which should be considered an adult."""
    assert is_adult(18) == True


# bug report 3
def test_r3_calculate_average():
    """Test that calculate_average returns 0 for an empty list to avoid ZeroDivisionError."""
    assert calculate_average([]) == 0


# bug report 4
def test_r4_remove_duplicates():
    """Test that remove_duplicates preserves the original order of elements."""
    items = [3, 1, 2, 3]
    result = remove_duplicates(items)
    assert result == [3, 1, 2], f"Expected [3, 1, 2] but got {result}"


# bug report 5
def test_r5_binary_search_single_element():
    """Test that binary_search returns the correct index for a single-element list."""
    assert binary_search([1], 1) == 0
