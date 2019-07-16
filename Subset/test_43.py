# Test condtions of the values of subset:

import Values

def test_canassertTrue():
    assert True

def test_subset_values():

    #Arrange:
    Array=[8,3,1,6]
    X=9
    expected=[set([8,1]),set([3,6])]

    #Act:
    actual=Values.Subset_Values(Array,X)

    #Assert:
    assert expected==actual


