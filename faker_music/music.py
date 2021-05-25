from random import choice
from faker.providers import BaseProvider
from .genres import genre_list
from .instruments import instrument_list


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
        return choice(genre_list)

    def music_genre(self):
        """
        Returns a string representing a musical genre.
        """
        my_choice = choice(genre_list)
        return my_choice["genre"]

    def music_subgenre(self):
        """
        Returns a string representing a musical subgenre.
        """
        while True:
            my_choice = choice(genre_list)
            if len(my_choice["subgenres"]) == 0:
                continue
            return choice(my_choice["subgenres"])

    def music_instrument_object(self):
        """
        Returns a randomly-chosen instrument dictionary. This is a
        dictionary whose first key is 'category', a string;
        and whose second key, "instruments", refers to a list of
        instruments in that category.

        Example:
        {
             "category": "electronics",
             "instruments": [
                 "Drum machine",
                 "Electric piano",
                 "Synthesizer"
             ]
        }
        """
        return choice(instrument_list)

    def music_instrument(self):
        """
        Returns a musical instrument in string format.
        """
        my_choice = choice(instrument_list)
        return choice(my_choice["instruments"])

    def music_instrument_category(self):
        """
        Returns an instrument category in string format.
        """
        my_choice = choice(instrument_list)
        return my_choice["category"]
