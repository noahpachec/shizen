
import genanki
import random

dict = {'ゲイ': "Gay"}



model_id = random.randrange(1 << 30, 1 << 31)

deck_id = random.randrange(1 << 30, 1 << 31)

my_model = genanki.Model(
    1091735104,
    'simple model',
    fields =[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Media'}
    ],
    
    templates=[
        {
            'name' : 'Card 1',
            'qfmt' : '{{Question}}<br>{{Media}}',
            'afmt' : '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])





deck = genanki.Deck( # deck
    1856076597,
    '[card-mine]'
)

package = genanki.Package(deck)
package.media_files = ['audio.mov']



# for key, value in dict.items():

#     note = genanki.Note(
#     model=my_model,
#     fields=[f'{key}', f'{value}']
    
#     )
#     deck.add_note(note)

note = genanki.Note(
    model=my_model,
    fields=["hello", "hello",'[sound:audio.mov]']
)

deck.add_note(note)


package.write_to_file('output.apkg')