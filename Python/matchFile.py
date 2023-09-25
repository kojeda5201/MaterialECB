import csv

# Leer el archivo de resultados y crear un diccionario de MAC a lista de usuarios
mac_to_users = {}
with open('resultados_piso5.csv', 'r') as resultados_file:
    resultados_reader = csv.DictReader(resultados_file)
    for resultado in resultados_reader:
        mac = resultado['ID Exclusivo'].lower()
        resultado_usuario = resultado['Usuario']
        if mac not in mac_to_users:
            mac_to_users[mac] = []
        if not resultado_usuario.strip():
            resultado_usuario = resultado["IP"]

        mac_to_users[mac].append(resultado_usuario)



# Leer el archivo de registros
registros = []
with open('C:\\Users\\jimoreno\\Documents\\Flex_Table_piso05.csv', 'r') as registros_file:
    registros_reader = csv.DictReader(registros_file)
    for registro in registros_reader:
        registros.append(registro)

# Agregar usuarios a registros correspondientes
for registro in registros:
    mac_address = registro['MAC Address'].lower()
    # print(mac_address)
    if mac_address in mac_to_users:
        usuarios = mac_to_users[mac_address]
        registro['Alias'] = "; ".join(usuarios) if 'Alias' not in registro else f"{registro['Alias']}; {', '.join(usuarios)}"

registros.sort(key=lambda x: x['Name'])

# Escribir los registros filtrados en el archivo resultadofinal.csv
# fieldnames = ['ReqID', 'IP Address', 'Instance', 'Port', 'Interface', 'Name', 'MAC Address', 'Alias']
with open('resultadofinal_piso5.csv', 'w', newline='') as resultadofinal_file:
    writer = csv.writer(resultadofinal_file)
    writer.writerow(['Name', 'MAC Address', 'Alias'])  # Escribir encabezados

    # for registro in registros:
    #     interface = registro['Name']
    #     mac_address = registro['MAC Address']
    #     alias = registro['Alias'].lower()
    #     writer.writerow([interface, mac_address, alias])
    for registro in registros:
        interface = registro['Name']
        if interface != "1:49":
            mac_address = registro['MAC Address']
            alias = registro['Alias'].lower()
            writer.writerow([interface, mac_address, alias])