import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_telegram_alert(detection_type, confidence, image_path=None):
    """Send fire detection alert to Telegram"""
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    
    if not bot_token or not chat_id:
        logger.error("Telegram credentials not configured")
        return False
    
    message = f"🚨 FIRE ALERT 🚨\n\nType: {detection_type.upper()}\nConfidence: {confidence:.1f}%"
    
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        response = requests.post(url, data={'chat_id': chat_id, 'text': message}, timeout=5)
        if response.status_code == 200:
            logger.info(f"Telegram alert sent: {detection_type} - {confidence:.1f}%")
            return True
        else:
            logger.error(f"Telegram API error: {response.text}")
            return False
    except Exception as e:
        logger.error(f"Failed to send Telegram alert: {e}")
        return False
