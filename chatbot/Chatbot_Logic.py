from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class AI:
    def __init__(self):
        self.openai = OpenAI(api_key=os.getenv('api_key'))
    def generate_response(self, prompt):
        response = self.openai.chat.completions.create(
            model="gpt-4o-mini",  # Model to use for image classification
            messages=[
                {"role": "system", "content": "You are a role-playing assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,  # Limit the response to 300 tokens
        )
        result = response.choices[0].message.content
        return {"message": result}
    
class ChatBot:
    def __init__(self):
        self.prompt = ''
        self.characters = ''
        self.ai = AI()
    def set_pramater(self, characters, prompt):
        self.characters = characters
        self.prompt = prompt
    def response(self):
        final_prompt = f'consider yourself as {self.characters} and reply to this "{self.prompt}"'
        response = self.ai.generate_response(final_prompt)
        return response