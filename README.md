# Keyl0gger Script for Educational Purposes
This project contains a simple keylogger script that captures keystrokes and sends them to a Discord webhook. It is intended solely for educational purposes to demonstrate how keyloggers work and how data can be captured from input devices.

# ⚠️ IMPORTANT: FOR EDUCATIONAL PURPOSES ONLY!
This script is NOT intended for malicious use. Do not use this script without explicit consent from the device owner. Unauthorized use of keylogging software may be illegal and unethical.

I do not take responsibility for any illegal actions or consequences that may arise from using this script.

# ❗ Disclaimer:
By using this code, you acknowledge that you are fully responsible for how it is used.
The author does not endorse or support any illegal activities such as unauthorized access to systems or devices.
Always seek permission before running any keylogging or monitoring software on someone else's system.
Features:
Monitors keyboard input events.
Sends captured keystrokes to a specified Discord webhook.
How It Works:
The script listens for keypress events using the hid library.
Every time a key is pressed, the script sends the keypress data to a specified Discord webhook.
There is a small delay between each keypress to avoid overwhelming the webhook with too many requests in a short time.
Requirements:
Python 3.x
urequests library (for sending HTTP requests)
hid library (for capturing keystrokes)
Installation:
Clone this repository:

bash
Kopírovať kód
git clone https://github.com/your-username/keylogger-script.git
cd keylogger-script
Install the required libraries:

bash
Kopírovať kód
pip install urequests hid
Modify the script:

Replace the WEBHOOK_URL variable with your own Discord webhook URL.
Run the script:

bash
Kopírovať kód
python keylogger.py
Usage:
The script will continuously run, listening for keypress events and sending the data to the specified Discord webhook.
Make sure you have the necessary permissions before running this script.
License:
This project is licensed under the MIT License - see the LICENSE file for details.

🚨 IMPORTANT NOTICE:
The author of this script is not responsible for any misuse or illegal activities that result from running or modifying this code. It is intended to be used for educational purposes only. Always comply with the laws and obtain proper consent before using this script in any real-world scenario.

