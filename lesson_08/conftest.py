import pytest
from YougileApi import YougileApi


base_url = 'https://ru.yougile.com/api-v2'
@pytest.fixture
def project():
    api = YougileApi(base_url)
    project_id = api.get_project_id()
    yield project_id
    api.delete_project(project_id)
