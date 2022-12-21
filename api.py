import requests


class Star_wars_characters:
    """Request Star Wars API"""
    def __init__(self):
        pass


    def get_characters(self):
        """Get characters links request"""

        star_wars_films_list = ['/1/', '/2/', '/3/', '/6/']
        url = 'https://swapi.dev/api/films'
        characters_links = set()
        characters_file = open('characters_file.txt', 'w', encoding='utf-8')

        for film in star_wars_films_list:
            get_url = url + film
            result_get = requests.get(get_url)
            assert result_get.status_code == 200, 'Test failed, status code not equal 200'
            print(f'Status code equal to expected: {result_get.status_code}')
            characters_json_links = result_get.json()
            characters_list = set(characters_json_links.get("characters"))
            characters_links.update(characters_list)

        print(f'Get characters links: {characters_links}')
        count = 0
        characters = []
        characters_file.write("All characters who played alongside Darth Vader:" + "\n")
        for link in characters_links:
            count += 1
            character_check = requests.get(link)
            character_json = character_check.json()
            characters.append(character_json.get("name"))
            characters_file.write(str(count) + '. ' + character_json.get("name") + '\n')

        characters_file.close()

        print(f'Final characters: {characters}')


get = Star_wars_characters()
get.get_characters()
