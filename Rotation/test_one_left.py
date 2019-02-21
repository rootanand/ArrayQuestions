# Test ccondition for rotating array to left by one bit:

import One_left

def test_canassertTrue():
    assert True

def test_one_left():
    
    #Arrange:
    Array=[7,9,2,4,0,5]
    expected=[9,2,4,0,5,7]

    #Act:
    actual=One_left.One_left(Array)

    #Assert:
    assert expected==actual