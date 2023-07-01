import pytest
from numerosAmigos import numeros_amigos

def test_1():
    assert numeros_amigos(2620,2924) == "2620 y 2924 son amigos"
    
def test_2():
    assert numeros_amigos(5020,5564) == "5020 y 5564 son amigos"
    
def test_3():
    assert numeros_amigos(17296,18416) == "17296 y 18416 son amigos"
    
def test_4():
    assert numeros_amigos(12285,14595) == "12285 y 14595 son amigos"
    
def test_5():
    assert numeros_amigos(66928,66992) == "66928 y 66992 son amigos"
    
def test_6():
    assert numeros_amigos(8,5) == "8 y 5  son amigos"

def test_7():
    assert numeros_amigos(3,9) == "3 y 9  son amigos"

def test_8():
    assert numeros_amigos(2,14) == "2 y 14 son amigos"
    
def test_9():
    assert numeros_amigos(125,56) == "125 y 56  son amigos"

def test_10():
    assert numeros_amigos(235,25) == "235 y 25  son amigos"
    
if __name__ == '_main_':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()
    test_10()