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
        # Returns a randomly-chosen genre dictionary. This is a
        # dictionary whose first key is 'genre', a string; 
        # and whose second key is 'subgenres', a list of strings.
        #
        # Example: 
        # {
        #      "genre": "Metal",
        #      "subgenres": [
        #          "Black Metal",
        #          "Goth Metal",
        #          "Thrash Metal"
        #      ]
        # }
        return choice(genre_list)

    def genre_name(self):
        return genre_object()
