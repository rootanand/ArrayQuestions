# Test condition for the Index of the Given Array: 

import X_index

def test_canassertTrue():
    assert True

def test_X_index():

    #arrange
    Array=[6,9,0,2,5,3,8]
    X=9
    expected=1

    #act
    actual=X_index.X_index(Array,X)

    #assert
    assert expected==actual
