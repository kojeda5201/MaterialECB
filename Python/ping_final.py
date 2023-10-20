import csv
import subprocess
import re
import nmap

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
    return ":".join(id_str[i:i + 2] for i in range(0, len(id_str), 2))


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


def load_ip_list(file_path):
    ip_list = []
    with open(file_path, 'r') as csvfile:
        next(csvfile)
        for row in csvfile:
            user = row.split(',')[1].split('.')[0].strip()
            ip = row.split(',')[0].strip()
            unique_id = row.split(',')[4].strip()
            ip_list.append((user, ip, unique_id, False))
    return ip_list


def load_ip_to_user(file_path):
    ip_to_user = {}
    with open(file_path, 'r') as csvfile:
        next(csvfile)
        for row in csvfile:
            user = row.split(';')[0].strip().lower()
            ip = row.split(';')[5]
            if ip not in ip_to_user:
                ip_to_user[ip] = set()
            ip_to_user[ip].add(user)
    return ip_to_user


def main():
    resultado_ping = {}
    active_users_array = get_active_users()
    ip_list = load_ip_list('Documents\\P5-v1.csv')
    ip_to_user = load_ip_to_user('Documents\\inventarioKS.csv')
    resultado_guardar = []

    for ip_array in active_users_array:
        for i, (user, ip, unique_id, is_Found) in enumerate(ip_list):
            if ip == ip_array:
                resultado = ping_ip(user)

                if resultado != 2 and resultado != 3 and resultado != ip and resultado != "dest":
                    resultado_ping.append(f"User: {user} no coincide con la dirección {ip}, responde dir: {resultado}")
                else:
                    resultado_ping_ip = ping_ip_v2(ip)
                    if resultado_ping_ip != 2 and resultado_ping_ip != 3 and resultado_ping_ip != ip and resultado_ping_ip != "dest":
                        resultado_ping.append(f"User: {user} no coincide con la dirección {ip}, responde dir: {resultado}")
                if resultado == ip or resultado_ping_ip == ip and any(ip == ip_array for _, ip, _, _ in ip_list):
                    ip_list[i] = (user, ip, unique_id, True)
                    active_users_dict[ip]["isFound"] = True
                    resultado_guardar.append(
                        {'Usuario': user.strip().lower(), 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})

    for i, (user, ip, _, is_Found) in enumerate(ip_list):
        if is_Found is False:
            user = user.strip().lower()
            user_found_kasp = False
            for users_set in ip_to_user.values():
                if user in users_set:
                    user_found_kasp = True
                    break
            if user_found_kasp:
                resultado_guardar.append({'Usuario': user, 'IP': ip, 'ID Exclusivo': format_unique_id(unique_id)})
                ip_list[i] = (user, ip, unique_id, True)

    print("\nDirecciones ip de nmap no encontradas en DHCP")
    # print(active_users_dict)
    for ip in active_users_dict:
        if active_users_dict[ip]['isFound'] == False:
            print(f"No esta en DHCP {ip}")

    print("\nUsuarios que no se encontraron en Nmap ni Kaspersky")
    for user, ip, _, is_Found in ip_list:
        if is_Found is False:
            print(f"{user}, {ip} no encontrados")

    if len(resultado_ping) != 0:
        print("\nUsuarios que no coinciden con IP")
        for text in resultado_ping:
            print(f"{text}")

    with open('resultados_piso5.csv', 'w', newline='') as csvfile:
        fieldnames = ['Usuario', 'IP', 'ID Exclusivo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in resultado_guardar:
            writer.writerow(row)


if __name__ == "__main__":
    main()
