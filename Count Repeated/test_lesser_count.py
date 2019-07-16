# Test case for the lesser count:

import Lesser_comparision

def test_canassertTrue():
    assert True

def test_Lesser():

    #Arrange:
    Array=[2,3,2,2,4,5]
    Integer=3
    expected=4

    #Act:
    actual=Lesser_comparision.Is_Lesser(Array,Integer)

    #Assert:
    assert expected==actual