class PlataformaBancaria:
    def __init__(self):
        self.usuarios = {
            "abiel": {"biometria": True, "codigo": "123456", "correo": "correo@example.com", "telefono": "8091234567"},
        }

    def autenticar(self, usuario, biometria, codigo):
        if usuario not in self.usuarios:
            return "Usuario no registrado"
        if not biometria:
            return "Autenticación biométrica fallida"
        if codigo != self.usuarios[usuario]["codigo"]:
            return "Código incorrecto"
        return "Inicio de sesión exitoso"

    def recuperar_cuenta(self, usuario, metodo, codigo):
        if usuario not in self.usuarios:
            return "Usuario no registrado"
        if metodo not in ["correo", "telefono"]:
            return "Debe seleccionar un método de recuperación"
        if codigo != self.usuarios[usuario]["codigo"]:
            return "Código incorrecto"
        return "Recuperación exitosa"

def iniciar_sesion(plataforma):
    print("--- Autenticación Multifactor (MFA) ---")
    print("Para un inicio de sesión exitoso, utilice:")
    print("Usuario: abiel")
    print("Código: 123456")
    
    usuario = input("Ingrese el usuario: ")
    biometria = input("¿Autenticación biométrica exitosa? (si/no): ").strip().lower() == "si"
    codigo = input("Ingrese el código dinámico: ")
    
    resultado = plataforma.autenticar(usuario, biometria, codigo)
    print("Resultado de autenticación:", resultado)
    return resultado

def recuperar_cuenta_interfaz(plataforma):
    print("--- Recuperación de Cuenta ---")
    usuario = input("Ingrese el usuario: ")
    metodo = input("Seleccione método de recuperación (correo/telefono): ")
    codigo = input("Ingrese el código de recuperación: ")
    
    resultado = plataforma.recuperar_cuenta(usuario, metodo, codigo)
    print("Resultado de recuperación de cuenta:", resultado)
    return resultado

if __name__ == "__main__":
    plataforma = PlataformaBancaria()
    iniciar_sesion(plataforma)
    recuperar_cuenta_interfaz(plataforma)
