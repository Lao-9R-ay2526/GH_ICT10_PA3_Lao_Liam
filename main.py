# Working with Dictionaries
from pyscript import display, document

def game_details(e):
    document.getElementById('result').innerHTML = ' '
    favorite_game = document.getElementById('dict').value.lower().strip()

    game_developers = {
        'roblox' : 'David Baszucki ',
        'codm' : 'TiMi Studio',
        'fnaf' : 'Scott Cawthon',
        'dmc5' : 'Capcom',

    } # Specifying Dictionaries

    game_check = favorite_game in game_developers

    display_message = ('Sorry This game is not on the list!', f'{game_developers[favorite_game]}')

    display(display_message[game_check], target="result")
    game_developers['dimenshot '] = 'Flexburg Games' # ADDING A NEW ELEMENT
    display(game_developers[favorite_game], target='result')

    list_with_tuples = [(1, 'a' ), (2, 'b'), (3, 'c')]
    tuple_with_strings = ('ab', 'cd', 'ef')
    list_with_strings = ['ax', 'by', 'cz']

    display(dict(list_with_tuples), target='result')
    display(dict(tuple_with_strings), target='result')
    display(dict(list_with_strings), target='result')

    keywords = [
        'say', 'jm', 'jay', 'mace',
    ]

    values = [ 'esguerra', 'piansay', 'estrada', 'mace']

    student_nicknames = dict(zip(keywords, values)) # Combining after Conversion

    display(student_nicknames, target='result')

    philadelphia = {
        'center' : 'Joel Embiid',
        'pf' : 'Lebron James',
        'sf' : 'Jaylen Bronw',
        'sg' : 'VJ Edgecomb',
        'pg' : 'Tyrese Maxey'
    }

    philadelphia['pg'] = 'Stephen Curry'
    del philadelphia['sg'] # Adding
    display(philadelphia, target='result')

    dict1 = {'x': 1 , 'y': 2, 'z': 3}
    dict2 = {'a': 4, 'b': 5 ,'c': 6}
    display(dict1 | dict2, target='result') # Combining
    merged_dict = {**dict1, **dict2 }

    display(merged_dict, target='result')
    display(len(merged_dict), target='result') # Counting

    artificial_intelligence = {
        'tony stark' : 'creator',
        'JARVIS' : 'AI1',
        'FRIDAY' : 'AI2',
        'EDITH' : 'AI3',
        'Ultron' : 'AI4'
    }

    display('Ultron' in artificial_intelligence, target='result') # checking
    display(artificial_intelligence.get('JARVIS'), target='result') # getting the value

    display(artificial_intelligence.keys(), target='result') # Getting all the keywords

    display(artificial_intelligence.values(), target='result') # getting all the values

    display(artificial_intelligence['tony stark'], target='result')