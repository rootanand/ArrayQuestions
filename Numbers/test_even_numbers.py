# Test condition for the even numbers in the given array:

import even_numbers

def test_canassertTrue():
    assert True

def test_even_numbers():

    #Arrange:
    Array=[8,1,5,3,6,4]
    expected=[8,6,4]

    #Act:
    actual=even_numbers.Even_numbers(Array)

    #Assert:
    assert expected==actual