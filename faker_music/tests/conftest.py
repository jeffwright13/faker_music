import pytest
from faker import Faker
from faker_music import MusicProvider


@pytest.fixture(scope="session")
def fake():
    fake = Faker()
    fake.add_provider(MusicProvider)
    return fake
