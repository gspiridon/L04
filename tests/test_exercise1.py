import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even():
    # Test that is_even returns True for even numbers (should be True)
    assert is_even(4) == True
    
    # Test that is_even returns False for odd numbers (should be False)
    assert is_even(3) == False
    
    # Test that is_even returns True for zero (even number)
    assert is_even(0) == True
    
    # Test that is_even returns False for negative even numbers
    assert is_even(-2) == False
    
    # Test that is_even returns True for negative odd numbers
    assert is_even(-3) == False


# bug report 2
def test_r2_rectangle_area():
    assert rectangle_area(4, 5) == 20, "Rectangle area should be width * height, not width + height"


# bug report 3
def test_r3_double_function():
    assert double(5) == 10, "double(5) should return 10, not 7"
