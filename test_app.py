import pytest
from app import validar_codigo_sistema

def test_codigo_valido():
    # Casos que devem passar
    assert validar_codigo_sistema("GOTHAM-0001") is True
    assert validar_codigo_sistema("GOTHAM-9999") is True

def test_codigo_invalido():
    # Casos que devem falhar
    assert validar_codigo_sistema("ARKHAM-1234") is False
    assert validar_codigo_sistema("GOTHAM-ABC") is False
    assert validar_codigo_sistema("12345") is False

def test_entrada_vazia():
    # Caso de borda
    assert validar_codigo_sistema("") is False
