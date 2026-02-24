#  دستیار هوش مصنوعی ماژولار برای وردپرس

این پروژه یه دستیار هوش مصنوعی ماژولار هست که با پایتون ساخته شده و می‌تونه از طریق REST API با وردپرس ارتباط بگیره و محتوای خودکار تولید کنه.

##  ویژگی‌ها
- اتصال به APIهای OpenAI/Groq
- تولید محتوای خودکار با  حرفه‌ای پرامپت ‌نویسی
- اتصال به وردپرس از طریق REST API
- ساختار ماژولار برای توسعه آسان
- پشتیبانی از زبان فارسی

##  تکنولوژی‌ها
- Python 3.8+
- OpenAI API
- WordPress REST API
- LangChain (قابل اضافه کردن)

##  نصب و راه‌اندازی
```bash
# کلون کردن پروژه
git clone https://github.com/Alborzkhan/ai-wordpress-assistant.git
cd ai-wordpress-assistant

# نصب کتابخانه‌ها
pip install -r requirements.txt

# تنظیم متغیرهای محیطی
cp sample_config.py .env
# حالا فایل .env رو با اطلاعات خودت پر کن

# اجرای برنامه
python assistant.py