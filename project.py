
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


lista = [ valor['name']  for valor in DATA if valor['language'] == 'python' ]
print(lista)


list_platzi_workers = [ valor['name']  for valor in DATA if valor['organization'] == 'Platzi' ]
print(list_platzi_workers)


list_platzi_workers_adults = list(filter(lambda valor : valor['age'] > 18, DATA))
print(list_platzi_workers_adults)

list_platzi_workers_adults_names = list(map(lambda valor : valor['name'], list_platzi_workers_adults))
print(list_platzi_workers_adults_names)


list_platzi_olds = list(map(lambda valor : valor | { 'old' :  valor['age'] > 70 }, DATA))
print(list_platzi_olds)


lista = list(map( lambda item: item['name']  ,filter(lambda valor :  valor['language'] == 'python',DATA)))
print(lista)

lista = list(map( lambda item: item['name']  ,filter(lambda valor :  valor['organization'] == 'Platzi',DATA)))
print(lista)


list_platzi_workers_adults = [valor['name'] for valor in DATA if valor['age']> 18 ]
print(list_platzi_workers_adults)


list_platzi_olds = [{**valor, **{'age': valor['age']> 70}}   for valor in DATA  ]
print(list_platzi_olds)