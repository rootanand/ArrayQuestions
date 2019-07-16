# Test case for the count of repeated numbers:

import Count_Repeated

def test_canassertTrue():
    assert True

def test_count_repeated():

    #arrange
    Array=[5,3,8,0,1,8]
    X=8
    expected=2

    #act
    actual=Count_Repeated.Count_Repeated(Array,X)

    #assert
    assert expected==actual