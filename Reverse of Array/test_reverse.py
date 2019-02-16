# Test condition for the reverse of the given array:

import rev_array

def test_canassertTrue():
    assert True

def test_reverse():

    #Arrange:
    Array=[8,0,1,4,2,9]
    expected=[9,2,4,1,0,8]

    #Act
    actual=rev_array.Rev_array(Array)

    #Assert:
    assert expected==actual