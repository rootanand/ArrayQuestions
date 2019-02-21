# Test condition for finding the value in the 3rd index after Two rotations of the given array:

def test_canassertTrue():
    assert True

# Rotation to right:

import index_right

def test_right_index():

    #Arrange:
    Array=[7,3,8,1,5]
    expected=3

    #Act:
    actual=index_right.Right_Index(Array)

    #Assert:
    assert expected==actual

# Rotation to Left:

import index_left

def test_left_index():

    #Arrange:
    Array=[7,2,8,4,6]
    expected=7

    #Act:
    actual=index_left.Left_Index(Array)

    #Assert:
    assert expected==actual