# Test condition for the subset of indices:

import Indices

def test_canassertTrue():
    assert True

def test_Subset_Index():

    #Arrange:
    Array=[8,3,1,6]
    X=9
    expected=[set([0,2]),set([1,3])]

    #Act:
    actual=Indices.Subset_Index(Array,X)

    #Assert:
    assert expected==actual
