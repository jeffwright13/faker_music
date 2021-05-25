def test_music_genre_object(fake):
    test_genre_obj = fake.music_genre_object()
    assert isinstance(test_genre_obj, dict)
    assert "genre" in test_genre_obj.keys()
    assert "subgenres" in test_genre_obj.keys()


def test_music_genre(fake):
    test_genre = fake.music_genre()
    assert isinstance(test_genre, str)
    assert len(test_genre) > 0


def test_music_subgenre(fake):
    test_subgenre = fake.music_subgenre()
    assert isinstance(test_subgenre, str)
    assert len(test_subgenre) > 0


def test_music_instrument_object(fake):
    test_instrument_obj = fake.music_instrument_object()
    assert isinstance(test_instrument_obj, dict)
    assert "category" in test_instrument_obj.keys()
    assert "instruments" in test_instrument_obj.keys()


def test_music_instrument(fake):
    test_instrument = fake.music_instrument()
    assert isinstance(test_instrument, str)
    assert len(test_instrument) > 0


def test_music_instrument_category(fake):
    test_instrument_category = fake.music_instrument_category()
    assert isinstance(test_instrument_category, str)
    assert len(test_instrument_category) > 0
