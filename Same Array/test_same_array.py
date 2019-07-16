#Test condition to find the same array:

import same_array

def test_canassertTrue():
    assert True

def test_Is_same():

     #Arrange:
    A=[8,3,1,9]
    B=[8,3,1,9]
    expected=True

     #Act:
    actual=same_array.Is_same(A,B)
    
    #Assert:
    assert expected==actual


