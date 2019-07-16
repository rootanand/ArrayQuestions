#Test condition to find the mode of the given array:

import Mode

def test_canassertTrue():
    assert True

def test_Mode():

    #Arrange
    Array=[7,2,0,2,2]
    expected=2

    #Act
    actual=Mode.Mode(Array)

    #Assert
    assert expected==actual
