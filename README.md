# SMB_Hacking
🔒 Exploración de SMB con Fuerza Bruta 🔒

Este script de Python utiliza técnicas de hacking ético para realizar pruebas de penetración en servidores SMB (Server Message Block) y explorar posibles vulnerabilidades. Te permite realizar un escaneo exhaustivo y una fase de fuerza bruta para probar la seguridad de un sistema SMB.

💡 Características del Script 💡

✅ Escaneo de Puertos: Utiliza la biblioteca nmap para escanear el puerto 445 (SMB) de la dirección IP objetivo y verificar si está abierto.

✅ Enumeración de Shares: Enumera los shares disponibles en el servidor SMB objetivo para descubrir información confidencial.

✅ Prueba de Autenticación Nula: Realiza una prueba de autenticación nula para verificar si es posible acceder al servidor SMB sin proporcionar credenciales.

✅ Fuerza Bruta de Credenciales: Realiza una fase de fuerza bruta utilizando un diccionario de contraseñas proporcionado por el usuario para intentar autenticarse en el servidor SMB con diferentes combinaciones de usuarios y contraseñas.

🚀 Cómo Ejecutar el Script 🚀

1️⃣ Requisitos Previos:

Asegúrate de tener Python 3 instalado en tu sistema.
Instala las dependencias necesarias ejecutando pip install nmap smbprotocol en tu terminal.
2️⃣ Clonar el Repositorio:

Clona este repositorio en tu máquina local usando el comando git clone <URL_del_repositorio>.
3️⃣ Configurar el Entorno:

Abre una terminal y navega hasta la carpeta del repositorio clonado.
Ejecuta el comando python smb_scan.py.
4️⃣ Ingrese los Detalles:

Se te pedirá que ingreses la dirección IP del servidor SMB objetivo.
Luego, se te solicitará el nombre de usuario y la ruta del diccionario de contraseñas.
5️⃣ Observa los Resultados:

El script comenzará a realizar pruebas de vulnerabilidad y exploración de SMB.
Te proporcionará información detallada sobre los resultados de cada prueba realizada.
🔒 Nota Importante 🔒

Este script debe utilizarse únicamente con permiso y para fines legales de pruebas de penetración y seguridad. El autor no se hace responsable de ningún mal uso o actividad ilegal.
