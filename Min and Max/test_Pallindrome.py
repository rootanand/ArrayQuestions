#Test Case to find Pallindrome or not:

import pallindrome

def test_canassertTrue():
    assert True

def test_pallindrome():

    #Arrange:

    Array=[4,2,4,6,1]
    expected=False

    #Act:

    actual=pallindrome.Pallindrome(Array)

    #Assert:

    assert expected==actual