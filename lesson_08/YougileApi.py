import requests
import uuid
from dotenv import load_dotenv
import os


load_dotenv()


class YougileApi:

    password = os.getenv('PASSWORD')
    email = os.getenv('LOGIN')

    def __init__(self, url):
        self.url = url
        self.token = os.getenv('YOUGILE_TOKEN')

    def get_company_id(self):
        base_url = 'https://ru.yougile.com/api-v2'
        auth = {
            "login": self.email,
            "password": self.password,
            "name": "SKY_PRO"
        }
        resp = requests.post(base_url + '/auth/companies', json=auth)
        company_id = resp.json()["content"][0]["id"]
        assert company_id is not None
        assert resp.status_code == 200
        return company_id

    def get_token(self):
        if self.token:
            return self.token
        company_id = self.get_company_id()
        body = {
            "login": self.email,
            "password": self.password,
            "companyId": company_id
            }
        resp = requests.post(self.url + '/auth/keys', json=body)
        token = resp.json()['key']
        self.token = token
        assert token is not None
        return self.token

    def get_user_id(self):
        # token = self.get_token()
        my_headers = {
                'Content-type': 'application/json',
                'Authorization': f'Bearer {self.token}'
                }
        resp = requests.get(self.url + '/users',
                            headers=my_headers)
        user = resp.json()["content"][0]['id']
        assert user is not None
        assert resp.status_code == 200
        return user

    def get_departments_id(self):
        # token = self.get_token()
        my_headers = {
                'Content-type': 'application/json',
                'Authorization': f'Bearer {self.token}'
                }
        resp = requests.get(self.url + '/departments',
                            headers=my_headers)
        department = resp.json()["content"][1]['id']
        assert department is not None
        assert resp.status_code == 200
        return department

    def get_idempotency(self):
        idempotency_key = str(uuid.uuid4())
        return idempotency_key

    def get_project_id(self):
        user_id = self.get_user_id()
        department = self.get_departments_id()
        # token = self.get_token()
        idempotency = self.get_idempotency()
        my_headers = {
                'Content-type': 'application/json',
                'Authorization': f'Bearer {self.token}'
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
        resp = requests.post(self.url + '/projects',
                             headers=my_headers, json=body)
        print(resp.json())
        project_id = resp.json()["id"]
        assert project_id is not None
        assert resp.status_code == 201
        return project_id

    def get_modified_project_id(self):
        # token = self.get_token()
        user_id = self.get_user_id()
        department = self.get_departments_id()
        project_id = self.get_project_id()
        my_headers = {
            'Content-type': 'application/json',
            'Authorization': f'Bearer {self.token}'
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
        resp = requests.put(f'{self.url}/projects/{project_id}',
                            headers=my_headers, json=body)
        print(resp.json())
        change_project_id = resp.json()["id"]
        assert change_project_id is not None
        assert resp.status_code == 200
        return change_project_id
