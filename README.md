# faker_music: music provider for Faker

An add-on provider for the Python Faker module to generate random and/or fake data for music-related categories.

## Description

`faker_music` provides music-related fake data for testing purposes.  The definition of "fake" in this context really means "random," as the musical data are real. Invocation of this module simply provides a random choice from the underlying real-world data.

No claims are made as to the accuracy or completeness of this data. However, suggestions/corrections/additional data are happily accepted.

Currently implemented:
- Music genres

Coming soon:
- Musical instruments

For future implementation:
- Composers
- Performers
- Band names (existing)
- Fake band name generator
- Theory (notes/scales/chord-types/progressions)
- ...?

## Installation

***Note: you must have the [Faker](https://pypi.org/project/Faker/) module already installed.***

Install with pip:
``` bash
pip install faker_music
```

Add as a provider to your Faker instance:
``` python
from faker import Faker
from faker_music import MusicProvider
fake = Faker()
fake.add_provider(MusicProvider)
```

Now you can start to generate data:
```python
fake.music_genre()
fake.music_subgenre()
etc...
```

## About the Music Genre Object

The `music_genre_object` is a dictionary consisting of a 'genre' string, and an associated 'subgenre' list. The purpose is to provide data that ties together a given genre with all of it known subgenres.

For example:

``` python
>>> fake.music_genre_object()
{'genre': 'Singer/Songwriter',
 'subgenres': ['Alternative Folk',
  'Contemporary Folk',
  'Contemporary Singer/Songwriter',
  'Indie Folk',
  'Folk-Rock',
  'Love Song',
  'New Acoustic',
  'Traditional Folk']}
```

## Generating Genre Data

The original data for this project (stored in `genres.py`) was lifted from https://www.musicgenreslist.com, and massaged into a format suitable for coding using `parser.py`, stored in [this Gist](https://gist.github.com/jeffwright13/ded48a18ba6db7feb47eea5892665d86).

