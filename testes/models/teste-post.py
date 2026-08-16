import pytest

from blog.factory import PostFactory

@pytest.fixture
def post_public():
    return PostFactory(title='pytest with factory')

@pyttest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'
