# Test case for Ith index after R rotations:

def test_canassertTrue():
    assert True

# Rotation to the Right:

import index_R_right

def test_Right():

    #Arrange:
    Array=[6,2,5,9,3]
    R=3
    I=2
    expected=3

    #Act:
    actual=index_R_right.by_right(Array,R,I)

    #Assert:
    assert expected==actual

# Rotation to the Left:

import index_R_left

def test_Left():

    #Arrange:
    Array=[4,9,1,0,3]
    R=2
    I=4
    expected=9

    #Act:
    actual=index_R_left.by_left(Array,R,I)

    #Assert:
    assert expected==actual