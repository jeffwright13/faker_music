import re
from pprint import pprint

check4 = lambda my_string: my_string[:4] == ' ' * 4
check8 = lambda my_string: my_string[:8] == ' ' * 8
check12 = lambda my_string: my_string[:12] == ' ' * 12

with open("music_genres_and_subgenres.txt", "r") as readfile:
    data = readfile.readlines()

genre_list = []
genre = subgenre = ""

for line in data:
    # print(f"genre, subgenre: {genre} {subgenre}")
    subgenre_list = []

    if check12(line):
        # print("Skipping 12 lines")
        continue
    if check4(line) and not check8(line):
        genre = line.strip()
        genre = re.sub("\(.*?\)","", genre).strip()
        # print(f"genre {genre} found")
        genre_list.append({"genre": genre, "subgenres": []})
        continue
    if check8(line) == True:
        subgenre = line.strip()
        subgenre = re.sub("\(.*?\)","", subgenre).strip()
        subgenre_list.append(subgenre)
        # print(f"subgenre {subgenre} found")
        genre_list[-1]["subgenres"].append(subgenre)

pprint(genre_list)
