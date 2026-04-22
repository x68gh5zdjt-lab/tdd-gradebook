from gradebook import letter_grade
from gradebook import is_passing
import pytest

@pytest.mark.parametrize("score, expected", [(95, 'A'),(85, 'B'),(75, 'C'),(67, 'D'),(42, 'F')])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected

def test_letter_grade_invalid_type():
    with pytest.raises(TypeError):
        letter_grade("Hello")

def test_is_passing_true():
    assert is_passing(75) == True

def test_is_passing_False():
    assert is_passing(45) == False

def test_is_passing_invalid_type():
     with pytest.raises(TypeError):
        is_passing("Mccuen is the goat")