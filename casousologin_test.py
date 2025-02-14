import pytest
from caso_uso_login import PlataformaBancaria

# Pruebas unitarias
@pytest.fixture
def plataforma():
    return PlataformaBancaria()

@pytest.mark.parametrize("usuario, biometria, codigo, esperado", [
    ("abiel", True, "123456", "Inicio de sesión exitoso"),
    ("abiel", False, "123456", "Autenticación biométrica fallida"),
    ("abiel", True, "000000", "Código incorrecto"),
    ("usuario_incorrecto", True, "123456", "Usuario no registrado"),
])
def test_autenticacion(plataforma, usuario, biometria, codigo, esperado):
    assert plataforma.autenticar(usuario, biometria, codigo) == esperado




    """
     Valida el inicio de sesión verificando si el usuario existe, la autenticación biométrica es exitosa
     y el código dinámico ingresado es correcto.
        
    Casos de uso cubiertos:
    - Validación de Autenticación Multifactor (MFA) en Plataforma Bancaria
    """


