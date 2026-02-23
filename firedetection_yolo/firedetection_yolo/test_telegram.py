import requests

BOT_TOKEN = "8529526114:AAHGJucaSgpPPETfPLOp9rr_K0NEGOVmYWE"
CHAT_ID = "5525246464"

message = "🚨 TEST FIRE ALERT 🚨\n\nType: FIRE\nConfidence: 85.5%\n\nThis is a test notification from your Fire Detection System!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(url, data={'chat_id': CHAT_ID, 'text': message})

if response.status_code == 200:
    print("SUCCESS: Telegram notification sent!")
    print("Check your Telegram app for the message.")
else:
    print(f"FAILED: {response.text}")
