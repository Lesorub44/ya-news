import os
import pytest
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yanews.settings')
django.setup()

@pytest.fixture
def news_item():
    from news.models import News
    return News.objects.create(title="Заголовок новости", text="Текст новости")