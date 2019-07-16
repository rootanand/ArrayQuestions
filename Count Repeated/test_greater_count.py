# Test case for the greater count:

import Greater_comparision

def test_canassertTrue():
    assert True

def test_Greater():

    #Arrange:
    Array=[2,3,2,2,4,5]
    Integer=3
    expected=3

    #Act:
    actual=Greater_comparision.Is_Greater(Array,Integer)

    #Assert:
    assert expected==actual