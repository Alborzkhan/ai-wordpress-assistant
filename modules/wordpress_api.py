import requests
import base64

class WordPressConnector:
    def __init__(self, site_url, username, password):
        self.site_url = site_url.rstrip('/')
        self.username = username
        self.password = password
        self.credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
        self.headers = {
            'Authorization': f'Basic {self.credentials}',
            'Content-Type': 'application/json'
        }
    
    def create_post(self, title, content, status='draft'):
        """ایجاد پست جدید در وردپرس"""
        endpoint = f"{self.site_url}/wp-json/wp/v2/posts"
        data = {
            'title': title,
            'content': content,
            'status': status
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=data)
            if response.status_code == 201:
                return {"success": True, "post_id": response.json().get('id')}
            else:
                return {"success": False, "error": response.text}
        except Exception as e:
            return {"success": False, "error": str(e)}
