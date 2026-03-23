import pytest
from main import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_not_palindrome():
    assert is_palindrome("hello") == False

def test_case_insensitive():
    assert is_palindrome("Racecar") == True

def test_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_empty_string():
    assert is_palindrome("") == True
