
def add(a, b):
    return a + b

def test_addition():
    assert add(2, 3) == 5
    assert add(1, 1) == 2
    assert add(-1, 1) == 0

import pytest


def testLogin():
    print("Login Successful")

def testLogoff():
    print("Log out successful")

def testClculation():
    assert 4 +4 == 8

def add(a, b):
    return a + b

def test_addition():
    assert add(2, 3) == 5
    assert add(1, 1) == 2
    assert add(-1, 1) == 0

def test_liste_noire():
    ma_liste = []
    assert len(ma_liste) == 0

def test_presence_liste():
    ma_liste = [1, 2, 3]
    assert 3 in ma_liste

def test_comparison_objet():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert a == b

