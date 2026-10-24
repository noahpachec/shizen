from recording_to_mp3 import convert_to_mp3
from recording_to_text import transcribe_media
from ai_api import 
import genanki
import uuid

from pathlib import Path

class DeckObject:
    def __init__(self, folder):
        self.cards = []
        self.folder = Path(folder)

    def addBatchAnswers(self):


    def loadFiles(self):
        #  Iterate through each file and assign it an object -> ('mined_recordings')
        for file in self.folder.iterdir():
            if not file.is_file():
               break
            card = CardObject(file)
            self.addCard(card)
  
    def addCard(self, card):
        self.cards.append(card)

    def printCards(self):
        print("[", end="")
        for i, card in enumerate(self.cards):
            if i != len(self.cards) - 1:
                print(f'{card.name}, ', end= " ")
            else:
                print(f'{card.name}', end="")
        print("]")

    def exportDeck(self):
        # Export all cards into a deck using GenAnki
        print("Exporting Deck...")

        
        anki_deck = genanki.Deck( # deck
            1856076597,
            '[card-mine]'
        )

        simple_model = genanki.Model(
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


        media_files = []

        for card in self.cards:
            note = genanki.Note(
                model=simple_model,
                fields=[
                    card.transcription,
                    card.transcription,
                    f'[sound:{card.mp3_media.name}]'
                ]
            )
            anki_deck.add_note(note)
            media_files.append(str(card.mp3_media))

        package = genanki.Package(anki_deck)
        package.media_files = media_files
        package.write_to_file('output.apkg')


        # clear mined_recordings folder
        for file in self.folder.iterdir():
            if file.is_file():
                file.unlink()



class CardObject:
    def __init__(self, original_media):
        self.id = uuid.uuid4().hex
        new_path = original_media.parent / (self.id + original_media.suffix)
        self.media_with_id = original_media.rename(new_path)
        self.mp3_media = Path(convert_to_mp3(self.media_with_id, 'converted_files/'))
        self.transcription = transcribe_media(self.mp3_media)
        self.name = self.media_with_id.name
        self.answer = "" # to be added by API

    def printFilePath(self):
        print(self.mp3_media)

    def printTranscription(self):
            print(self.transcription)

    def getFileName(self):
        return self.mp3_media.name






deck = DeckObject('mined_recordings')
deck.loadFiles()
deck.printCards()
deck.exportDeck()