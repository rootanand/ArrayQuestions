# Test condition for the Kth Smallest number in the given array:

import Kth_smallest

def test_canassertTrue():
    assert True

def test_Smallest():

    #Arrange:
    Array=[8,2,5,1,9,4]
    K=4
    expected=5

    #Act:
    actual=Kth_smallest.Kth_Smallest(Array,K)

    #Assert:
    assert expected==actual