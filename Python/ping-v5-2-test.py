ip_to_user = {}
with open('C:\\Users\\jimoreno\\Documents\\Listadeequipos.csv', 'r') as csvfile:
    next(csvfile)
    for row in csvfile:
        user = row.split(';')[0].strip().lower()
        ip = row.split(';')[5]
        print(ip, user)
        ip_to_user[ip].append(user)
for ip in ip_to_user:
    print(ip)