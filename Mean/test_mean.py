# Test condition to find the mean of the given array:

import Mean_of_the_Array

def test_canassertTrue():
    assert True

def test_mean():

    #Arrange:
    Array=[6,0,1,7,11,4,3]
    expected=4

    #Actual:
    actual=Mean_of_the_Array.Mean_of_Array(Array)

    #Assert:
    assert expected==actual