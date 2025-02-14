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





