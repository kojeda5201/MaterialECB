import csv
import subprocess
import re
import nmap
from natsort import natsorted


active_users_dict = {}
def get_active_users():
    active_users = []
    nm = nmap.PortScanner()
    try:

        nm.scan(hosts="172.22.45.1-255", arguments="-sn")

        for host in nm.all_hosts():
            active_users_dict[host] = {"isFound": False}
            active_users.append(host)
    except Exception as e:
        print("Error al ejecutar el escaneo:", e)

    return active_users

active_users_array = get_active_users()
def ping_ip(ip):
    try:
        output = subprocess.check_output(["ping", "-n", "2", ip])
        output_str = output.decode("utf-8", errors="replace")
        match = re.search(r'\[(\d+\.\d+\.\d+\.\d+)\]', output_str)

        if "Host de destino inaccesible" in output_str:
            return "dest"
        elif match:
            return match.group(1)
        else:
            return 2
    except subprocess.CalledProcessError:
        return 3

def format_unique_id(id_str):
    return ":".join(id_str[i:i+2] for i in range(0, len(id_str), 2))


def ping_ip_v2(ip):
    try:
        output = subprocess.check_output(["ping", "-n", "2", ip])
        output_str = output.decode("utf-8", errors="replace")
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', output_str)

        if "Host de destino inaccesible" in output_str:
            return "dest"
        elif match:
            return ip
        else:
            return 2
    except subprocess.CalledProcessError:
        return 3
ip_list = []

with open('Documents\\P5.csv', 'r') as csvfile:
    next(csvfile)
    for row in csvfile:
        user = row.split(',')[1].split('.')[0].strip()
        ip = row.split(',')[0].strip()
        unique_id = row.split(',')[4].strip()
        is_Found = False
        ip_list.append((user, ip, unique_id, is_Found))

ip_to_user = {}
with open('Documents\\Listadeequipos.csv', 'r') as csvfile:
    next(csvfile)
    for row in csvfile:
        user = row.split(';')[0].strip().lower()
        ip = row.split(';')[5]
        if ip not in ip_to_user:
            ip_to_user[ip] = set()
        ip_to_user[ip].add(user)


resultado_ping = []
resultado_innacesible = []
resultado_innacesibleV2 = []
resultado_user = []
resultado_guardar = []
resultado_kas = []


for ip_array in active_users_array:



    for i, (user, ip, unique_id, is_Found) in enumerate(ip_list):
        if ip == ip_array:
            # print(f"{user, ip, unique_id}")
            ip_list[i] = (user, ip, unique_id, True)
            resultado_guardar.append({'Usuario': user.strip().lower(), 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id), })
            break
# print("\n")
# for user, ip, unique_id, is_Found in ip_list:
#     if is_Found == True:
#         print(f"{user, ip, unique_id, is_Found}")

# for i, (user, ip, unique_id, is_Found) in enumerate(ip_list):
#
#     if is_Found == False:
#         resultado = ping_ip(user)
#         if resultado != 2 and resultado != 3:
#             if resultado != ip and resultado != "dest":
#                  resultado_ping.append(f"User: {user} no coincide con al direccion {ip}, responde dir: {resultado}")
#                 # print(f"User: {user} no coincide con al direccion {ip}, responde dir: {resultado}")
#             elif resultado == "dest":
#                 user = user.strip().lower()
#                 user_found_kasp = False  # Inicializa una bandera para indicar si se encontró al usuario en algún conjunto
#                 for users_set in ip_to_user.values():
#                     if user in users_set:
#                         user_found_kasp = True
#                         break
#                 if user_found_kasp:
#                     resultado_guardar.append({'Usuario': user.strip().lower(), 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id), })
#                     # ip_list[i] = (user, ip, unique_id, True)
#                 else:
#                     resultado_innacesibleV2.append(f"User: {user} innacesible con {ip}")
#                 # resultado_guardar.append({'Usuario': user, 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})
#
#             elif resultado == ip:
#                 resultado_guardar.append({'Usuario': user, 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})
#                 # ip_list[i] = (user, ip, unique_id, True)
#         else:
#             resultado_ip = ping_ip_v2(ip)
#             # print(f"resultado_ip {resultado_ip} and ip {ip}")
#             if resultado_ip != 2 and resultado_ip != 3 and resultado_ip != ip and resultado_ip != "dest":
#                 resultado_user.append(f"Responde IP: {resultado_ip} no coincide con la del DHCP {ip}, usuario: {user}")
#                 # print(f"User: {user} no respondió al ping ni a la IP {ip}")
#                 if ip_to_user[resultado_ip] != user.lower():
#                     resultado_kas.append(
#                         f"Kaspersky Responde IP: {resultado_ip} esta ip asociada a {ip_to_user[resultado_ip]} no coincide con la del DHCP {ip} para usuario: {user} segun kars")
#             elif resultado_ip == "dest":
#                 user_found_kasp = False  # Inicializa una bandera para indicar si se encontró al usuario en algún conjunto
#                 for ip in ip_to_user:
#                     user_found_kasp = True
#                     break
#                 if user_found_kasp:
#                     resultado_guardar.append(
#                         {'Usuario': user.strip().lower(), 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id), })
#                     # ip_list[i] = (user, ip, unique_id, True)
#                 else:
#                     resultado_innacesible.append(f"IP: {ip} innacesible con {user}")
#             elif resultado_ip == 2 or resultado_ip == 3:
#                 user_found_kasp = False  # Inicializa una bandera para indicar si se encontró al usuario en algún conjunto
#                 for ip in ip_to_user:
#                     user_found_kasp = True
#                     break
#                 if user_found_kasp:
#                     resultado_guardar.append(
#                         {'Usuario': user.strip().lower(), 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id), })
#                     ip_list[i] = (user, ip, unique_id, True)
#                 else:
#                     print(f"User: {user} no respondió al ping ni a la IP {ip}")
#             elif resultado_ip == ip:
#                 # ip_list[i] = (user, ip, unique_id, True)
#                 resultado_guardar.append({'Usuario': user, 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})

        # user = user.strip().lower()
        # user_found_kasp = False  # Inicializa una bandera para indicar si se encontró al usuario en algún conjunto
        # for users_set in ip_to_user.values():
        #     if user in users_set:
        #         user_found_kasp = True
        #         break
        # if user_found_kasp:
        #     resultado_guardar.append({'Usuario': user, 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})
        # else:
        #     print(f"Usuario {user} no esta dentro de kasperky")



    # print()
    # for user, ip, unique_id, is_Found in ip_list:
    #     if is_Found == True:
    #         print(user, True)
#
# if("172.22.45.125" in ip_to_user):
#     print(f"{True} user 172.22.45.125")


# if len(resultado_ping) != 0:
#     print("\nUsuarios que no coinciden con ip")
#     for text in resultado_ping:
#         print(f"{text}")
#
# if len(resultado_user)!= 0 :
#     print("\nIP no coincide con ip del DHCP")
#     for text_ip in resultado_user:
#         print(f"{text_ip}")
#
# if len(resultado_kas)!= 0:
#     print("\n IP no coincide con ip del DHCP comprobado con Kaspersky")
#     for text in resultado_kas:
#         print(f"{text}")
#
# if len(resultado_innacesibleV2) != 0:
#     print("\nUsuario innacesibles")
#     for text_inacc in resultado_innacesibleV2:
#         print(f"{text_inacc}")
#
# if len(resultado_innacesible) != 0:
#     print("\nIP innacesibles")
#     for text_inacc in resultado_innacesible:
#         print(f"{text_inacc}")
#
# with open('resultados_piso5.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Usuario', 'IP', 'ID Exclusivo']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for row in resultado_guardar:
#         writer.writerow(row)

print()
print("Usarios no econtrados")
for user, ip, unique_id, is_Found in ip_list:
    if is_Found == False:
        print(user, ip)


    # if user in [ip for _, ip, _ in ip_list]:


# for user, ip, unique_id in ip_list:
#     user = user.strip().lower()
#     user_found_kasp = False  # Inicializa una bandera para indicar si se encontró al usuario en algún conjunto
#     # print()s
#
#
#     for users_set in ip_to_user.values():
#         if user in users_set:
#             user_found_kasp = True
#             break
#
#     if user_found_kasp:
#
#         resultado = ping_ip(user)
#         if resultado != 2 and resultado != 3:
#             if resultado != ip and resultado != "dest":
#                 resultado_ping.append(f"User: {user} no coincide con al direccion {ip}, responde dir: {resultado}")
#                 # print(f"User: {user} no coincide con al direccion {ip}, responde dir: {resultado}")
#             elif resultado == "dest":
#                 resultado_innacesibleV2.append(f"User: {user} innacesible con {ip}")
#                 resultado_guardar.append({'Usuario': user, 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})
#             elif resultado == ip:
#                 resultado_guardar.append({'Usuario': user, 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})
#         else:
#             resultado_ip = ping_ip_v2(ip)
#             # print(f"resultado_ip {resultado_ip} and ip {ip}")
#             if resultado_ip != 2 and resultado_ip != 3 and resultado_ip != ip and resultado_ip != "dest" :
#                 resultado_user.append(f"Responde IP: {resultado_ip} no coincide con la del DHCP {ip}, usuario: {user}")
#                 # print(f"User: {user} no respondió al ping ni a la IP {ip}")
#                 if ip_to_user[resultado_ip] != user.lower():
#                     resultado_kas.append(f"Kaspersky Responde IP: {resultado_ip} esta ip asociada a {ip_to_user[resultado_ip]} no coincide con la del DHCP {ip} para usuario: {user} segun kars")
#             elif resultado_ip == "dest":
#                 resultado_innacesible.append(f"IP: {ip} innacesible con {user}")
#             elif resultado_ip == 2 or resultado_ip == 3:
#                 print(f"User: {user} no respondió al ping ni a la IP {ip}")
#             elif resultado_ip == ip:
#                 resultado_guardar.append({'Usuario': user, 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})
#     else:
#         print(f"Usuario {user} no esta dentro de kasperky")
#
#
# if len(resultado_ping)!= 0 :
#     print("\nUsuarios que no coinciden con ip")
#     for text in resultado_ping:
#         print(f"{text}")
#
# if len(resultado_user)!= 0 :
#     print("\nIP no coincide con ip del DHCP")
#     for text_ip in resultado_user:
#         print(f"{text_ip}")
#
# if len(resultado_kas)!= 0:
#     print("\n IP no coincide con ip del DHCP comprobado con Kaspersky")
#     for text in resultado_kas:
#         print(f"{text}")
#
# if len(resultado_innacesibleV2) != 0:
#     print("\nUsuario innacesibles")
#     for text_inacc in resultado_innacesibleV2:
#         print(f"{text_inacc}")
#
# if len(resultado_innacesible) != 0:
#     print("\nIP innacesibles")
#     for text_inacc in resultado_innacesible:
#         print(f"{text_inacc}")
#
# with open('resultados_piso5.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Usuario', 'IP', 'ID Exclusivo']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for row in resultado_guardar:
#         writer.writerow(row)

