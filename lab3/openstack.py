import requests
import json


def get_token():
    print('Получение токена, введите данные для авторизации')
    user = {
        'username': input('Username:\n'),
        'password': input('Password:\n'),
        'url': input('URL в формате ip\n')
    }
    responce = requests.post(
        'http://'+user['url']+':5000/v3/auth/tokens',
        json={
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": user['username'],
                            "domain": {"name": "Default"},
                            "password": user['password']
                        }
                    }
                },
                "scope": {
                    "project": {
                        "domain": {"id": "default"},
                        "name": "admin"
                    }
                }
            }
        },
        headers={'Content-type': 'application/json'}
    )
    print('Токен:', responce.headers['X-Subject-Token'])
    return responce.headers['X-Subject-Token'], 'http://'+user['url']


def get_server_list(token, url):
    responce = requests.get(
        url+':8774/v2.1/servers',
        headers={
            'Content-type': 'application/json',
            'X-Subject-Token': token,
            'X-Auth-Token': token,
        }
    )
    data = json.loads(responce.content)
    return data


def get_flavors_list(token, url):
    responce = requests.get(
        url+':8774/v2.1/flavors',
        headers={
            'Content-type': 'application/json',
            'X-Subject-Token': token,
            'X-Auth-Token': token,
        }
    )
    data = json.loads(responce.content)
    return data


def get_images_list(token, url):
    responce = requests.get(
        url+':8774/v2.1/images',
        headers={
            'Content-type': 'application/json',
            'X-Subject-Token': token,
            'X-Auth-Token': token,
        }
    )
    data = json.loads(responce.content)
    return data


def get_volumes_list(token, url):
    responce = requests.get(
        url+':8774/v2.1/os-volumes',
        headers={
            'Content-type': 'application/json',
            'X-Subject-Token': token,
            'X-Auth-Token': token,
        }
    )
    data = json.loads(responce.content)
    return data


def get_networks_list(token, url):
    responce = requests.get(
        url+':8774/v2.1/os-tenant-networks',
        headers={
            'Content-type': 'application/json',
            'X-Subject-Token': token,
            'X-Auth-Token': token,
        }
    )
    data = json.loads(responce.content)
    return data


def get_id_by_name_label(input_data, name):
    for i in input_data.values():
        for j in i:
            for k in j:
                if j[k] == name:
                    return j['id']


def create_server(VM, token, url):
    responce = requests.post(
        url+':8774/v2.1/servers',
        headers={
            'Content-type': 'application/json',
            'X-Subject-Token': token,
            'X-Auth-Token': token,
        },
        json={
                "server": {
                    "name": VM['name'],
                    "imageRef": VM['image'],
                    "flavorRef": VM['flavor'],
                    "networks": [{
                        "uuid": VM['network']
                    }],
                    "key_name": "my_key",
                    "security_groups": [{
                            "name": "default"
                    }]
                }
        }
    )
    return responce


def main():
    token, url = get_token()
    server_list = get_server_list(token, url)
    flavors_list = get_flavors_list(token, url)
    images_list = get_images_list(token, url)
    volumes_list = get_volumes_list(token, url)
    networks_list = get_networks_list(token, url)
    print(
        '\nСписок названий существующих ВМ: ',
        ', '.join([i['name'] for i in server_list['servers']])
    )
    print(
        '\nСписок названий существующих Flavors: ',
        ', '.join([i['name'] for i in flavors_list['flavors']])
    )
    print(
        '\nСписок названий существующих образов: ',
        ', '.join([i['name'] for i in images_list['images']])
    )
    print(
        '\nСписок названий существующих томов: ',
        ', '.join([i['displayName'] for i in volumes_list['volumes']])
    )
    print(
        '\nСписок названий существующих сетей в проекта: ',
        ', '.join([i['label'] for i in networks_list['networks']])
    )
    print('Введите данные для создания ВМ из предложенных выше:')
    VM = {
        'name': input('Vms name:\n'),
        'flavor': get_id_by_name_label(flavors_list, input('Flavor:\n')),
        'image': get_id_by_name_label(images_list, input('Image:\n')),
        'network': get_id_by_name_label(networks_list, input('Network:\n'))
    }
    print(create_server(VM, token, url).status_code)
    print(
        '\nСписок названий существующих ВМ: ',
        ', '.join([i['name'] for i in get_server_list(token, url)['servers']])
    )


if __name__ == '__main__':
    main()
