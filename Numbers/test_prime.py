# Test condition for finding prime numbers in the given array:

import prime_numbers

def test_canassertTrue():
    assert True

def test_prime():

    #Arrange:
    Array=[11,5,9,6,2]
    expected=[11,5,2]

    #Act:
    actual=prime_numbers.prime_array(Array)

    #Assert:
    assert expected==actual