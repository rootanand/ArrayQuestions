# Test case for removing duplicates from the given array:

def test_canassertTrue():
    assert True

import remove_duplicates

def test_duplicates():

    #Arrange:
    Array=[5,2,6,2,3,5,6,2]
    expected=[5,2,6,3]

    #Act:
    actual=remove_duplicates.duplicates(Array)

    #Assert:
    assert expected==actual