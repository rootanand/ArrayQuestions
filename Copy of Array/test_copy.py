# Test case for the copy of the given array:

import copy

def test_canassertTrue():
    assert True

def test_copy():

    #Arrange
    Array=[1,7,2,5,4,9]
    expected=[1,7,2,5,4,9]

    #Act
    actual=copy.copy(Array)

    #Assert:
    assert expected==actual