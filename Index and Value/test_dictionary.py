#Test condition for creating dictionary in python:

import dictionary

def test_canassertTrue():
    assert True

def test_dictionary():
     
     #Arrange:
     Array=[6,2,84,9]
     expected={0:6,1:2,2:84,3:9}

     #Actual:
     actual=dictionary.Dictionary(Array)

     #Assert
     assert expected==actual