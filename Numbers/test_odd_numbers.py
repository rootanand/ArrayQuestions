# Test condition for the odd numbers in the given array:

import odd_numbers

def test_canassertTrue():
    assert True

def test_odd_numbers():

    #Arrange:
    Array=[8,1,5,3,6,4]
    expected=[1,5,3]

    #Act:
    actual=odd_numbers.Odd_numbers(Array)

    #Assert:
    assert expected==actual