import pytest
import requests
from YougileApi import YougileApi


base_url = 'https://ru.yougile.com/api-v2'


def test_create_project():
    api = YougileApi(base_url)
    api.get_company_id()
    token = api.get_token()
    user_id = api.get_user_id()
    department = api.get_departments_id()
    idempotency = api.get_idempotency()
    my_headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
    body = {
        "title": "Luna",
        "users": {
            user_id: "worker"
        },
        "departments": {
            department: {
                "manager": "admin",
                "member": "worker"
            }
        },
        "idempotencyKey": idempotency}
    resp = requests.post(base_url + '/projects', headers=my_headers, json=body)
    print(resp.json())
    project_id = resp.json()["id"]
    assert project_id is not None
    assert resp.status_code == 201


# Негативный тест с отправкой пустого значения в "title"
def test_create_project_negative():
    api = YougileApi(base_url,)
    api.get_company_id()
    token = api.get_token()
    user_id = api.get_user_id()
    department = api.get_departments_id()
    idempotency = api.get_idempotency()
    my_headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
    body = {
        "title": "",
        "users": {
            user_id: "worker"
        },
        "departments": {
            department: {
                "manager": "admin",
                "member": "worker"
            }
        },
        "idempotencyKey": idempotency}
    resp = requests.post(base_url + '/projects', headers=my_headers, json=body)
    print(resp.json())
    # project_id = resp.json()["id"]
    # assert project_id is not None
    assert resp.status_code == 400


def test_change_project():
    api = YougileApi(base_url,)
    token = api.get_token()
    user_id = api.get_user_id()
    department = api.get_departments_id()
    project_id = api.get_project_id()
    my_headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
    body = {
            "deleted": True,
            "title": "Luna",
            "users": {
                user_id: "worker"
            },
            "departments": {
                department: {
                    "manager": "admin",
                    "member": "worker"
                }
            },
        }
    resp = requests.put(f'{base_url}/projects/{project_id}',
                        headers=my_headers, json=body)
    print(resp.json())
    change_project_id = resp.json()["id"]
    assert change_project_id is not None
    assert resp.status_code == 200


# Негативный тест с отправкой неверного id отдела
def test_change_project_negative():
    api = YougileApi(base_url)
    token = api.get_token()
    user_id = api.get_user_id()
    # department = api.get_departments_id()
    project_id = api.get_project_id()
    my_headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + token
        }
    body = {
            "deleted": True,
            "title": "Luna",
            "users": {
                user_id: "worker"
            },
            "departments": {
                '111': {
                    "manager": "admin",
                    "member": "worker"
                }
            },
        }
    resp = requests.put(f'{base_url}/projects/{project_id}',
                        headers=my_headers, json=body)
    print(resp.json())
    change_project_id = resp.json()["message"]
    assert change_project_id == 'Отдел не найден: 111'
    assert resp.status_code == 400


def test_get_by_id():
    api = YougileApi(base_url)
    token = api.get_token()
    modified_id = api.get_modified_project_id()
    my_headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer ' + token
            }
    resp = requests.get(f'{base_url}/projects/{modified_id}',
                        headers=my_headers)
    print(resp.json())
    get_id = resp.json()["id"]
    assert get_id == modified_id
    assert resp.status_code == 200


# Негативный тест с отправкой неверного id отдела
def test_get_by_id_negative():
    api = YougileApi(base_url)
    token = api.get_token()
    # modified_id = api.get_modified_project_id()
    my_headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer ' + token
            }
    resp = requests.get(f'{base_url}/projects/111',
                        headers=my_headers)
    print(resp.json())
    get_id = resp.json()["message"]
    assert get_id == 'Проект не найден'
    assert resp.status_code == 404
