# Test case for Rotating the given array by K times:

def test_canasssertTrue():
    assert True

# For rotating right:

import K_rotations_right

def test_rotate_right():

    #Arrange:
    Array=[6,2,8,1,0,5]
    K=3
    expected=[1,0,5,6,2,8]

    #Act:
    actual=K_rotations_right.by_right(Array,K)

    #Assert:
    assert expected==actual


# For rotating Left:

import K_rotations_left

def test_rotate_left():

    #Arrange:
    Array=[6,9,2,0,1]
    K=2
    expected=[2,0,1,6,9]

    #Act:
    actual=K_rotations_left.by_left(Array,K)

    #Assert:
    assert expected==actual