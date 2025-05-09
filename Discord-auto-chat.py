import requests
import time

user_token = 'YOUR_USER_TOKEN_HERE'
channel_id = 'YOUR_CHANNEL_ID_HERE'
message = "This is an automated message from a Python script."

headers = {
    'Authorization': user_token,
    'Content-Type': 'application/json'
}

url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

payload = {
    'content': message
}

while True:
    response = requests.post(url, headers=headers, json=payload)
    print(f"Sent: {message} | Status: {response.status_code}")
    time.sleep(60)
