# Test condition for finding the largest numgber in an array:

import Largest

def test_canassertTrue():
    assert True

def test_Largest():

    #Arrange
    Array=[7,0,1,11,2]
    expected=1

    #Act
    actual=Largest.Largest_in_Array(Array)

    #Assert
    expected==actual
