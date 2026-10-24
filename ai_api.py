from openai import OpenAI
from pathlib import Path


class AnswerGenerator:
    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-5.5"
        self.batch_size = 15
        self.prompt = Path('prompts/card_answer_prompt.txt').read_text(encoding="utf-8")


    def createAnswers(self, cards):
        



# sentence = "今日は大学に行かなきゃいけない"

# response = client.responses.create(
#     model="gpt-5.5",
#     input=f"""
#         Break down this Japanese sentence for a learner.

#         Sentence:
#         {sentence}

#         Explain:
#         - important words/chunks
#         - grammar
#         - nuance
#         - no full English translation
#         - keep it concise
#         """
# )

# print(response.output_text)

