from faker.providers import BaseProvider
from random import choice, choices, randint
from .genres import genre_list


class MusicProvider(BaseProvider):
    """
    A Provider for music-related data.

    Typical use:
    >>> from faker import Faker
    >>> from faker_music import MusicProvider
    >>> fake = Faker()
    >>> fake.add_provider(MusicProvider)
    >>> fake.music_genre()
    >>> fake.music_subgenre()
    >>> etc...
    """

    def music_genre_object(self):
        """
        Returns a randomly-chosen genre dictionary. This is a
        dictionary whose first key is 'genre', a string;
        and whose second key is 'subgenres', a list of strings.

        Example:
        {
             "genre": "Metal",
             "subgenres": [
                 "Black Metal",
                 "Goth Metal",
                 "Thrash Metal"
             ]
        }
        """
        g = choice(genre_list)
        return g

    def music_genre(self):
        """
        Returns a string representing a musical genre.
        """
        g = choice(genre_list)
        return g["genre"]

    def music_subgenre(self):
        """
        Returns a string representing a musical subgenre.
        """
        while True:
            g = choice(genre_list)
            if len(g["subgenres"]) == 0:
                continue
            else:
                return choice(g["subgenres"])
