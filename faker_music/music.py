from faker.providers import BaseProvider
from random import choice, choices, randint
from genres import genre_list

class MusicProvider(BaseProvider):
    """
    A Provider for music-related data.

    >>> from faker import Faker
    >>> from faker_music import MusicProvider
    >>> fake = Faker()
    >>> fake.add_provider(MusicProvider)
    """

    def genre_object(self):
        g = choice(genre_list)
        return g

    def genre_name(self):
        g = choice(genre_list)
        return g["genre"]
