# Test ccondition for rotating array to left by one bit:

import One_right

def test_canassertTrue():
    assert True

def test_one_right():
    
    #Arrange:
    Array=[7,9,2,4,0,5]
    expected=[5,7,9,2,4,0]

    #Act:
    actual=One_right.One_right(Array)

    #Assert:
    assert expected==actual