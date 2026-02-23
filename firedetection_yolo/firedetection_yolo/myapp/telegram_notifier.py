import requests
from django.conf import settings

def send_telegram_alert(detection_type, confidence, image_path=None):
    """Send fire detection alert to Telegram"""
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    
    if not bot_token or not chat_id:
        return False
    
    message = f"🚨 FIRE ALERT 🚨\n\nType: {detection_type.upper()}\nConfidence: {confidence:.1f}%"
    
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        requests.post(url, data={'chat_id': chat_id, 'text': message}, timeout=5)
        return True
    except:
        return False
