# Test Conditon for the existence of subset in the given Array
 
import IsExists

def test_canassertTrue():
    assert True

def test_IsExists():

    #Arrange:
    Array=[8,3,1,6]
    X=9
    expected=True

    #Act
    actual=IsExists.Is_Exists(Array,X)

    #Assert
    assert expected==actual