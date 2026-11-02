# import pytest
# import requests
# base_url = 'https://ru.yougile.com/api-v2'
# auth = {
#     "login": "SeAN777@yandex.ru",
#     "password": "topsecret09041988",
#     "name": "SKY_PRO"
# }


# @pytest.fixture
# def get_company_id():
#     resp = requests.post(base_url + '/auth/companies', json=auth)
#     company_id = resp.json()["content"][0]["id"]
#     assert company_id is not None
#     assert resp.status_code == 200
#     return company_id


# def get_token(get_company_id):
#     body = {
#         "login": "SeAN777@yandex.ru",
#         "password": "topsecret09041988",
#         "companyId": get_company_id
#     }
#     resp = requests.post(base_url + '/auth/keys', json=body)
#     token = resp.json()['key']
#     assert token is not None
#     return token
