from app import 
validar_codigo_sistema

def test_codigo_valido():
    assert 
validar_codigo_sistema("GOTHAM-0001") is True

def test_codigo_invalido():
    assert 
validar_codigo_sistema("ARKHAM-1234") is False
