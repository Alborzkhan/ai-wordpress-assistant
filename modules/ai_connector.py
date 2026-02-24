import openai
import os

class AIConnector:
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        openai.api_key = self.api_key
    
    def generate_content(self, prompt, max_tokens=500):
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "تو یک دستیار تولید محتوای حرفه‌ای هستی."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"خطا: {str(e)}"
