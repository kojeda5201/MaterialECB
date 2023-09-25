import subprocess
import re

def ping_ip_v2(ip):
    try:
        output = subprocess.check_output(["ping", "-n", "2", ip])
        output_str = output.decode("utf-8", errors="replace")  # Decodificar la salida a una cadena con manejo de errores
        
        # Buscar dirección IP en el formato de salida específico
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', output_str)
        
        if match:
            return match.group(1)  # Devolver la dirección IP capturada
        else:
            return None
    except subprocess.CalledProcessError:
        return None

ip = "172.22.44.203"  # Cambia esto a la dirección que quieras verificar
responding_ip = ping_ip(ip)

if responding_ip:
    print(f"La dirección IP que responde a {ip} es {responding_ip}")
else:
    print(f"No se pudo obtener una respuesta de {ip}")
