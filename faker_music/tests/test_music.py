from faker import Faker
from faker_music import MusicProvider

fake = Faker()
fake.add_provider(MusicProvider)


def test_music_genre_object():
    test_genre_obj = fake.music_genre_object()
    assert isinstance(test_genre_obj, dict)
    assert "genre" in test_genre_obj.keys()
    assert "subgenre" in test_genre_obj.keys()


def test_music_genre():
    test_genre = fake.music_genre()
    assert isinstance(test_genre, str)
    assert len(test_genre) > 0


def test_music_subgenre():
    test_subgenre = fake.music_subgenre()
    assert isinstance(test_subgenre, str)
    assert len(test_subgenre) > 0
