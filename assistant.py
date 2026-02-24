#!/usr/bin/env python3
"""
دستیار هوش مصنوعی ماژولار برای وردپرس
 نویسنده : Alborz Rad
"""

from modules.ai_connector import AIConnector
from modules.wordpress_api import WordPressConnector
import os
from dotenv import load_dotenv

load_dotenv()

class AIAssistant:
    def __init__(self):
        self.ai = AIConnector(api_key=os.getenv("OPENAI_API_KEY"))
        self.wp = WordPressConnector(
            site_url=os.getenv("WP_URL"),
            username=os.getenv("WP_USER"),
            password=os.getenv("WP_APP_PASSWORD")
        )
    
    def generate_and_publish(self, topic):
        """تولید محتوا درباره یک موضوع و انتشار در وردپرس"""
        print(f"⏳ در حال تولید محتوا درباره: {topic}")
        prompt = f"یک مقاله 500 کلمه‌ای درباره {topic} بنویس. زبان: فارسی"
        content = self.ai.generate_content(prompt)
        
        print("✅ محتوا تولید شد")
        print("📤 در حال ارسال به وردپرس...")
        
        result = self.wp.create_post(
            title=f"مقاله درباره {topic}",
            content=content,
            status="draft"  # پیش‌نویس
        )
        
        if result["success"]:
            print(f"✅ پست با موفقیت ایجاد شد. آیدی: {result['post_id']}")
        else:
            print(f"❌ خطا: {result['error']}")

def main():
    print("🤖 دستیار هوش مصنوعی وردپرس")
    print("-" * 40)
    
    assistant = AIAssistant()
    
    while True:
        topic = input("موضوع مقاله رو وارد کن (یا 'exit' برای خروج): ")
        if topic.lower() == 'exit':
            break
        
        assistant.generate_and_publish(topic)

if __name__ == "__main__":
    main()