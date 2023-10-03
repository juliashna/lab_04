import pytest
import lib

lists = [[2, 1, 3, 5, 6, 7], [2, 5, 7, 10], [2, 7, 5]]

def test_CountElements_good():
    assert lib.count_common_elements(lists) == 3

def test_CountElements_bad():
    assert lib.count_common_elements(lists) == 5