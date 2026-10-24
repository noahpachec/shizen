from openai import OpenAI
from pathlib import Path
import json


class AnswerGenerator:
    def __init__(self):

        self.client = OpenAI()
        self.model = "gpt-5.5"
        self.batch_size = 5

        base_dir = Path(__file__).parent
        self.base_prompt = (
            base_dir / "prompts" / "card_answer_prompt.txt"
        ).read_text(encoding="utf-8")


    def createAnswers(self, cards):

        card_lookup = {
            card.id: card
            for card in cards
        }

        for batch in self.chunkCards(cards):
            
            cards_json = [
                {
                    "id": card.id,
                    "sentence": card.transcription
                }

                for card in batch
            ]

            response = self.client.responses.create(
                model=self.model,
                input=self.base_prompt + "\nCards:\n " + json.dumps(cards_json, ensure_ascii=False)
            )

            print(response.output_text)

            results = json.loads(response.output_text)

            for result in results:
                card_lookup[result["id"]].answer = result["answer"]


    def chunkCards(self, cards):
        for i in range(0, len(cards), self.batch_size):
            yield cards[i:i + self.batch_size]
