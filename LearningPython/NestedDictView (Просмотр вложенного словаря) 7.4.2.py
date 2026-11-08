server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
for key, value in server_data.items():
    print(f'{key}:')
    for item, data in value.items():
        print(f'\t{item}: {data}')
        
