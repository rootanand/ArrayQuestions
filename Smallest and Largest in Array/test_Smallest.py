#Test Condition for the smallest element in array:

import Smallest

def test_canassertTrue():
    assert True

def test_Smallest():
     
     #Arrange:
     Array=[8,4,9,2,5,11]
     expected=11

     #Act
     actual=Smallest.Smallest_in_Array(Array)

     #Assert
     assert expected==actual

