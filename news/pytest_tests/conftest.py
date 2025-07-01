import pytest
from news.models import News

@pytest.fixture
def news_item():
    return News.objects.create(title='Заголовок новости', text='Тестовый текст')

@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client