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
active_users = get_active_users()
for ip in active_users:
    print(ip)



# import csv
# import subprocess
# import re

# def ping_ip_v2(ip):
#     try:
#         output = subprocess.check_output(["ping", "-n", "2", ip])
#         output_str = output.decode("utf-8", errors="replace")
#         match = re.search(r'(\d+\.\d+\.\d+\.\d+)', output_str)
#
#         if "Host de destino inaccesible" in output_str:
#             return "dest"
#         elif match:
#             return ip
#         else:
#             return 2
#     except subprocess.CalledProcessError:
#         return 3
#
# print(f"resultado {ping_ip_v2('172.22.44.196')}")
