import subprocess

# Lee las direcciones IP desde el archivo CSV
ip_list = []
with open('ping-ipv1.csv', 'r') as csvfile:
    for line in csvfile:
        ip = line.strip()  # Elimina espacios en blanco y saltos de línea
        ip_list.append(ip)

# Función para verificar si una dirección IP responde al ping
    def ping_ip(ip):
        try:
            subprocess.check_output(["ping", "-n", "2", ip])
            return True
        except subprocess.CalledProcessError:
            return False

# Realiza el ping a cada dirección IP y muestra aquellas que no responden
for ip in ip_list:
    if not ping_ip(ip):
        print(f"La dirección IP {ip} no respondió al ping.")
