

import genanki
import random

dict = {'こんいちは': "Hi", 'うまい': "Yummy", '今日どう？': "How was today?"}

model_id = random.randrange(1 << 30, 1 << 31)

deck_id = random.randrange(1 << 30, 1 << 31)

my_model = genanki.Model(
    model_id,
    'simple model',
    fields =[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    
    templates=[
        {
            'name' : 'Card 1',
            'qfmt' : '{{Question}}',
            'afmt' : '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])





deck = genanki.Deck( # deck
    deck_id,
    'shiranai'
)



for key, value in dict.items():

    note = genanki.Note(
    model=my_model,
    fields=[f'{key}', f'{value}']
    
    )
    deck.add_note(note)


genanki.Package(deck).write_to_file('output.apkg')