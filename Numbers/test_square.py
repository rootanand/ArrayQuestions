# Test condition for the perfect square in the given array:

import perfect_sq

def test_canassertTrue():
    assert True

def test_square():

    #Arrange:
    Array=[16,5,9,6,2]
    expected=[16,9]

    #Act:
    actual=perfect_sq.perfect_sq_array(Array)

    #Assert:
    assert expected==actual