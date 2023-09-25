import csv
import subprocess
import re

def ping_ip(ip):
    try:
        output = subprocess.check_output(["ping", "-n", "2", ip])
        output_str = output.decode("utf-8", errors="replace")  # Decodificar la salida a una cadena con manejo de errores
        match = re.search(r'\[(\d+\.\d+\.\d+\.\d+)\]', output_str)  # Buscar dirección IP entre corchetes
        if match:
            return match.group(1)  # Devolver la dirección IP capturada
        else:
            return 2
    except subprocess.CalledProcessError:
        return 3

# option = int(input('Ingrese la opción de ip:\n1: ip\n2: usuario\n-> '))
option = 2

def ping_ip_v2(ip):
    try:
        subprocess.check_output(["ping", "-n", "2", ip])
        return True
    except subprocess.CalledProcessError:
        return False

ip_list = []
with open('C:\\Users\\jimoreno\\Documents\\DHCPv3.csv', 'r') as csvfile:
    next(csvfile)
    for row in csvfile:
        if option == 1:
            ip = row.split(',')[0].strip()
            user = row.split(',')[1].split('.')[0].strip()
        elif option == 2:
            user = row.split(',')[1].split('.')[0].strip()
            ip = row.split(',')[0].strip()

        ip_list.append((user, ip))
        
resultado_ping = []
resultado_user = []
for user, ip in ip_list:
    resultado = ping_ip(user)
    if resultado != 2 and resultado != 3:
        if resultado != ip:
            resultado_ping.append(f"User: {user} no coincide con al direccion {ip}, responde dir: {resultado}")
            # print(f"User: {user} no coincide con al direccion {ip}, responde dir: {resultado}")
    else:
        resultado_ip = ping_ip(ip)
        # print(f"resultado_ip {resultado_ip} and ip {ip}")
        if resultado_ip != 2 and resultado_ip !=3:
            resultado_user.append(f"Responde IP: {resultado_ip} no coincide con la del DHCP {ip}, usuario: {user}")  
        else:
            print(f"User: {user} no respondió al ping para ni a la IP {ip}")
            
if len(resultado_ping)!= 0 :
    print("\nUsuarios que no coinciden con ip\n")
    for text in resultado_ping:
        print(f"{text}")

if len(resultado_user)!= 0 :
    print("\nIP no coincide con ip del DHCP\n")
    for text_ip in resultado_user:
        print(f"{text_ip}")
