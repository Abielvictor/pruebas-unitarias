import pytest
from caso_uso_validacion import PlataformaBancaria

@pytest.fixture
def plataforma():
    return PlataformaBancaria()

@pytest.mark.parametrize("usuario, metodo, codigo, esperado", [
    ("abiel", "correo", "123456", "Recuperación exitosa"),
    ("abiel", "telefono", "123456", "Recuperación exitosa"),
    ("abiel", "correo", "000000", "Código incorrecto"),
    ("usuario_incorrecto", "correo", "123456", "Usuario no registrado"),
    ("abiel", "", "123456", "Debe seleccionar un método de recuperación"),
])
def test_recuperacion(plataforma, usuario, metodo, codigo, esperado):
    assert plataforma.recuperar_cuenta(usuario, metodo, codigo) == esperado



"""
Simula el proceso de recuperación de cuenta en la plataforma bancaria, solicitando usuario,
    método de recuperación y código de verificación.
    
Casos de uso cubiertos:
- Validación de Recuperación de Cuenta en Plataforma Bancaria
 """