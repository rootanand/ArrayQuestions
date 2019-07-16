# Test case for rotation of the array by the two bits:

import two_right

def test_canassertTrue():
    assert True

def test_two_right():

    #Arrange:
    Array=[8,3,0,1,2]
    expected=[1,2,8,3,0]

    #Act:
    actual=two_right.Two_right(Array)

    #Assert:
    assert expected==actual