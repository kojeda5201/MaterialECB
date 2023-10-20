import socket

def resolve_hostnames(ip_list):
    hostnames = {}
    for ip in ip_list:
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            hostnames[ip] = hostname
        except socket.herror:
            hostnames[ip] = "N/A"
    return hostnames

# Lista de direcciones IP que obtuviste de nmap
ip_list = ["172.22.45.48"]

# Obtener los nombres de host asociados a las direcciones IP
hostnames = resolve_hostnames(ip_list)

# Imprimir los resultados
for ip, hostname in hostnames.items():
    print(f"IP: {ip}, Nombre de host: {hostname}")
