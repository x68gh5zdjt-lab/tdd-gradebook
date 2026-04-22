from gradebook import letter_grade
from gradebook import is_passing
from gradebook import average
from gradebook import curved_score
import pytest

@pytest.mark.parametrize("score, expected", [(95, 'A'),(85, 'B'),(75, 'C'),(67, 'D'),(42, 'F')])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected

def test_letter_grade_invalid_type():
    with pytest.raises(TypeError):
        letter_grade("Hello")

def test_is_passing_true():
    assert is_passing(75) == True

def test_is_passing_false():
    assert is_passing(45) == False

def test_is_passing_invalid_type():
     with pytest.raises(TypeError):
        is_passing("Int only please")

def test_average_works():
    assert average([80,90,70]) == 80.00 #DEVISON RETURNS A FLOAT

def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])

def test_average_not_a_list():
    with pytest.raises(TypeError):
        average("Not a list")

def test_average_but_item():
    with pytest.raises(TypeError):
        average(80, "ninety" , 70)

def test_curved_score_bald():
    assert curved_score(80, 5) == 85

def test_curved_score_cap():
    assert curved_score(95 10) == 100