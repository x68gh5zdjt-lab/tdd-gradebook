from gradebook import letter_grade
import pytest

@pytest.mark.parametrize("score, expected", [(95, 'A'),(85, 'B'),(75, 'C'),(67, 'D'),(42, 'F')])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected

