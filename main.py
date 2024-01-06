def get_smart_superhero(names):
    top_intelligence = -1
    top_name = ''
    for name in names:
        r = requests.get(f'https://www.superheroapi.com/api.php/2619421814940190/search/{name}')
        data = r.json()
        intelligence = int(data['results'][0]['powerstats']['intelligence'])
        print(name, intelligence)
        if intelligence > top_intelligence:
            top_intelligence = intelligence
            top_name = name

    print(f'{top_name} - самый умный, его интеллект равен {top_intelligence}.')


get_smart_superhero(['Hulk', 'Captain America', 'Thanos'])