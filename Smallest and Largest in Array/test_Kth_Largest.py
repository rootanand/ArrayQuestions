# Test condition for the Kth Largest number in the given array:

import Kth_largest

def test_canassertTrue():
    assert True

def test_Largest():

    #Arrange:
    Array=[8,2,5,1,9,4]
    K=4
    expected=4

    #Act:
    actual=Kth_largest.Kth_Largest(Array,K)

    #Assert:
    assert expected==actual