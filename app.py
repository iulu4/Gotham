import re

def validar_codigo_sistema(codigo: 
str) -> bool:
    padrao = r"^GOTHAM-\d{4}$"
    if re.match(padrao, 
str(codigo)):
        return True
    return False

if __name__ == "__main__":
    print(f"Validando: 
{validar_codigo_sistema('GOTHAM-1234')}")
