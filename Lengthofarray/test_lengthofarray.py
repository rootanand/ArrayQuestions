#Test condition for length of the given array:

import Lengthofarray

def test_canassertTrue():
    assert True

def test_len_of_array():
    
    #arrange
    A=[4,6,2]
    expected=3

    #act
    actual=Lengthofarray.lengthofarray(A)

    #assert
    assert expected==actual