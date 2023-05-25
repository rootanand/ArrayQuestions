# Test condition for counting largest and smallest array:

import count_smallest
import count_largest

def test_canassertTrue():
    assert True

def test_smallest():
     
     #Arrange:
     Array=[7,9,2,3,8,2,2]
     expected=3

     #Act
     actual=count_smallest.count_smallest(Array)

     #Assert:
     assert expected==actual

def test_largest():
     
     #Arrange:
     Array=[7,9,2,3,8,2,9]
     expected=2

     #Act
     actual=count_largest.count_largest(Array)

     #Assert:
     assert expected==actual