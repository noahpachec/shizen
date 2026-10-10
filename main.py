from recording_to_mp3 import convert_to_mp3
from recording_to_text import transcribe_media
from pathlib import Path

class FlashCard:
    def __init__(self, original_media):
        self.original_media = original_media
        self.mp3_media = Path(convert_to_mp3(original_media, 'converted_files/'))
        self.transcription = transcribe_media(self.mp3_media)

    def printFilePath(self):
        print(self.mp3_media)

    def printTranscription(self):
            print(self.transcription)

    def getFileName(self):
        return self.mp3_media.name


a = FlashCard('mined_recordings/audio.mov')
a.printFilePath()
a.printTranscription()

