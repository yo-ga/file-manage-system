import pytest

from django.contrib.auth import get_user_model

from file_manager.models import File


@pytest.fixture
def fake_user():
    user_model = get_user_model()
    user = user_model(username='test', password='test')
    user.save()
    return user


@pytest.mark.django_db
def test_create_user_home(fake_user):
    user = fake_user
    assert user
    assert File.objects.filter(name='Home', owner=user.pk, directory=None, file_type='D').exists()
