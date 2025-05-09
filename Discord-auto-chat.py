import requests
import time
import random

user_token = 'YOUR_USER_TOKEN_HERE'
channel_id = 'YOUR_CHANNEL_ID_HERE'

headers = {
    'Authorization': user_token,
    'Content-Type': 'application/json'
}

url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

# Friendly messages (Good Morning removed!)
messages = [
    "Hii everyone 👋",
    "yoo Wassup !"
]             #You can add more messages as you want  but remember that they should be within "" and separate by a (,) except the last message should not have a (,) at its end

def send_message(message):
    typing_time = random.uniform(1.0, 2.0)    #You can change the message typing time here
    print(f"Typing for {typing_time:.2f} seconds...")
    time.sleep(typing_time)

    payload = {'content': message}
    response = requests.post(url, headers=headers, json=payload)
    print(f"Sent: {message} | Status: {response.status_code}")

    # 10% chance to delete & resend message
    if random.random() < 0.1:
        msg_id = response.json().get("id")
        if msg_id:
            time.sleep(1)
            requests.delete(f"{url}/{msg_id}", headers=headers)
            print(f"Deleted message: {message}")
            time.sleep(2)
            response = requests.post(url, headers=headers, json={'content': message + " *fixed"})
            print(f"Re-sent: {message} *fixed")

    return response.status_code

# 💡 Loop through shuffled messages forever
while True:
    phase = messages.copy()
    random.shuffle(phase)  # Shuffle order each phase
    print(f"\n--- New Phase: {len(phase)} messages ---\n")

    for msg in phase:
        send_message(msg)
        delay = random.randint(2,4)    #You can change the message sending time delay 
        print(f"Waiting {delay} seconds...\n")
        time.sleep(delay)
