# Test condition to find the second largest and smallest number in the given array:

import second_largest_smallest

def test_canassertTrue():
    assert True

def test_Largest_smallest():

    #Arrange:
    Array=[9,4,2,5,1]
    largest_expected=5
    smallest_expected=2

    #Act:
    largest_actual=second_largest_smallest.second_largest(Array)
    smallest_actual=second_largest_smallest.second_smallest(Array)

    #Assert:
    assert largest_expected==largest_actual
    assert smallest_expected==smallest_actual