# Test condition for the repeated Numbers: 

import Repeated

def test_canassertTrue():
    assert True

def test_isRepeated():

     #arrange
    
    Array=[5,6,3,4,3,9]
    X=9
    expected=False

    #act   
    actual=Repeated.Is_repeated(Array,X)

    #assert
    assert expected==actual


