import re

def validar_codigo_sistema(codigo: str) -> bool:
    """
    Simula a validação de um código de sistema no padrão GOTHAM-0000.
    """
    padrao = r"^GOTHAM-\d{4}$"
    if re.match(padrao, codigo):
        return True
    return False

if _name_ == "_main_":
    print(f"Teste de validação: {validar_codigo_sistema('GOTHAM-1234')}")
