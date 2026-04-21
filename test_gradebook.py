from gradebook import letter_grade

def test_letter_grade_A():
    assert letter_grade(95) == "A"

def test_letter_grade_F():
    assert letter_grade(42) == "F"

@pytest.mark.paramitize("score, expected", [95, "A"], [85, "B"], [75, "C"], [65, "D"], [45, "F"])
def test_letter_grade (score, expected):
    assert letter_grade(score) == expected

