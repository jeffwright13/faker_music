# faker_music: music provider for Faker

An add-on provider for the Python Faker module to generate random and/or fake data for music-related categories.

## Description

`faker_music` provides music-related fake data for testing purposes.  The definition of "fake" in this context really means "random," as the musical data are real. Invocation of this module simply provides a random choice from the underlying real-world data.

No claims are made as to the accuracy or completeness of this data. However, suggestions/corrections/additional data are happily accepted.

Currently implemented:
- Music genres
- Musical instruments

Coming soon:
- Composers
- Performers

For future implementation:
- Band names (existing)
- Fake band name generator
- Theory (notes/scales/chord-types/progressions)
- ...?

## Installation

From PyPi:

``` bash
pip install faker_music
```

From source code:

``` bash
git clone <faker_music_repo>
cd faker_music
pip install --upgrade pip setuptools wheel
python setup.py sdist bdist_wheel

cd dist
pip install --no-index <wheelfile>
  or
pip install <tarball>

    (e.g. pip install ubemsapi-1.1.6-py3-none-any.whl
    (e.g. pip install ubemsapi-1.1.6.tar.gz)
```


## Execution

Set up an environment with required modules (incuding the [Faker](https://pypi.org/project/Faker/) module):
``` bash
pip install -r requirements.txt
```

Add as a provider to your Faker instance:
``` python
>>>from faker import Faker
>>>from faker_music import MusicProvider
>>>fake = Faker()
>>>fake.add_provider(MusicProvider)
```

Now you can start to generate data:
```python
>>>fake.music_genre()
>>>fake.music_subgenre()
>>>fake.music_instrument()
>>>fake.music_instrument_category()
```

## About faker_music Objects

The `music_genre_object` is a dictionary consisting of a 'genre' string, and an associated 'subgenre' list. The purpose is to provide data that ties together a given genre with all of it known subgenres.

For example:

``` python
>>> fake.music_genre_object()

{'genre': 'Singer/Songwriter',
 'subgenres': [
  'Alternative Folk',
  'Contemporary Folk',
  'Contemporary Singer/Songwriter',
  'Indie Folk',
  'Folk-Rock',
  'Love Song',
  'New Acoustic',
  'Traditional Folk']}
```

Similarly, The `music_instrument_object` is a dictionary consisting of an instrument 'category' string, and an associated 'instrument' list. The purpose is to provide data that ties together a given caegory with all of it known instruments.

For example:

``` python
>>> fake.music_instrument_object()

{'category': 'electronics',
 'instruments': [
  'Drum machine',
  'Electric guitar',
  'Keyboard',
  'Synthesizer',
  'Theremin',
  'Turntable']}
```

## Data Sources

Original data for this project (stored in `genres.py`, `instruments.py`) was lifted from https://www.musicgenreslist.com and [Wikipedia](https://simple.wikipedia.org/wiki/List_of_musical_instruments), and massaged into a format suitable for coding using the `genre_parser.py` and `instrument_parser.py` code [found here](https://gist.github.com/jeffwright13/ded48a18ba6db7feb47eea5892665d86).

## Acknowlegements

- I would like to thank the maintainer of the [faker_airtravel](https://github.com/dkotschessa/faker_airtravel/) repository, since I used its structure to create this one.
- Big thanks also to [Bob Belderbos](https://github.com/bbelderbos) for his expert guidance in getting this litte project off the ground.
