# Test case for the identical elements:

import identical

def test_canassertTrue():
    assert True

def test_identical_array():

    #Arrange:
    A=[3,41,5,64,2,1]
    B=[3,41,5,6,2,1]
    expected=2

    #Act:
    actual=identical.identical(A,B)

    #Assert:
    assert expected==actual