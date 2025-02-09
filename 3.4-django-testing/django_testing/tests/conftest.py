import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    """Фикстура для клиента API."""
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make("Student", **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make("Course", **kwargs)
    return factory