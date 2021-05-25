from faker import Faker
from faker_music import MusicProvider

fake = Faker()
fake.add_provider(MusicProvider)


def test_music_genre_object():
    test_genre_obj = fake.music_genre_object()
    assert isinstance(test_genre_obj, dict)
    assert "genre" in test_genre_obj.keys()
    assert "subgenres" in test_genre_obj.keys()


def test_music_genre():
    test_genre = fake.music_genre()
    assert isinstance(test_genre, str)
    assert len(test_genre) > 0


def test_music_subgenre():
    test_subgenre = fake.music_subgenre()
    assert isinstance(test_subgenre, str)
    assert len(test_subgenre) > 0


def test_music_instrument_object():
    test_instrument_obj = fake.music_instrument_object()
    assert isinstance(test_instrument_obj, dict)
    assert "category" in test_instrument_obj.keys()
    assert "instruments" in test_instrument_obj.keys()


def test_music_instrument():
    test_instrument = fake.music_instrument()
    assert isinstance(test_instrument, str)
    assert len(test_instrument) > 0


def test_music_instrument_category():
    test_instrument_category = fake.music_instrument_category()
    assert isinstance(test_instrument_category, str)
    assert len(test_instrument_category) > 0
