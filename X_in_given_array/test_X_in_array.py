# Test condition for checking given X in array:

import X_in_Array

def test_canassertTrue():
    assert True

def test_X_in_array():

    #arrange
    Array=[6,9,0,2,5,1,7]
    X=8
    expected=False

    #act
    actual=X_in_Array.X_in_array(Array,X)

    #assert
    assert expected==actual
