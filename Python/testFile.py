import nmap
from natsort import natsorted

active_users_dic = {}  # Diccionario para almacenar usuarios activos


def get_active_users():
    active_users = []  # Diccionario para almacenar usuarios activos

    nm = nmap.PortScanner()

    try:
        # Realizar un escaneo de hosts en el rango especificado
        nm.scan(hosts="172.22.45.1-255", arguments="-sn")

        # Iterar sobre los resultados y obtener direcciones IP activas
        for host in nm.all_hosts():
            active_users_dic[host] = {"isFound": False}
            active_users.append(host)
    except Exception as e:
        print("Error al ejecutar el escaneo:", e)

    return active_users


# Llamar a la función para obtener el diccionario de usuarios activos
# active_users_array = get_active_users()

ip_list = []
ip_to_user = {}
# i = 0

with open('Documents\\P5.csv', 'r') as csvfile:
    next(csvfile)
    for row in csvfile:
        user = row.split(',')[1].split('.')[0].strip()
        ip = row.split(',')[0].strip()
        unique_id = row.split(',')[4].strip()
        is_Found = False
        ip_list.append((user, ip, unique_id, is_Found))

with open('Documents\\Listadeequipos.csv', 'r') as csvfile:
    next(csvfile)
    for row in csvfile:
        user = row.split(';')[0].strip().lower()
        ip = row.split(';')[5]
        if ip not in ip_to_user:
            ip_to_user[ip] = set()
        ip_to_user[ip].add(user)

for i, (user, ip, unique_id, is_Found) in enumerate(ip_list):
    found = False
    for user_set in ip_to_user.values():
        if user in user_set or ip in ip_to_user:
            found = True
            break
    if found == False:
        print(f"{user} no encontrado")

# for x,y,z in ip_list:
#     print(x,y,z)
# keys_sort_active_users_dic = list(active_users_dic.keys())
# keys_sort_active_users_dic.sort()
# sort_active_users_dic = {i: active_users_dic[i] for i in keys_sort_active_users_dic}

# sorted_keys = natsorted(active_users_dic.keys())
#
# print(sorted_keys)

# for user in sorted_keys:
#     print(user)
#     if user in [item[1] for item in ip_list] :
#         print(True)
#     else:
#         print(False)
# # Imprimir el diccionario de usuarios activos
# print(active_users_array)
# for user in active_users_array:
#     print(user)


# i = 0
# print("\nDic active")
# # for user, bool in active_users_dic.items():
# for user in sorted_keys:
#     if (i <= 2):
#         active_users_dic[user]["isFound"] = True
#     i += 1
#     print(user, active_users_dic[user]["isFound"])

    # if status == "up":
    #     print(f"IP: {ip}, Estado: Activo")
    # else:
    #     print(f"IP: {ip}, Estado: Inactivo")
