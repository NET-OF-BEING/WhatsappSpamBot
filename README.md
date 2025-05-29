
# WhatsApp Auto Message Sender

This is a Python script that uses Selenium to automatically send a specified message to a specific contact on WhatsApp Web at set intervals.

## ⚙️ Features

- Automates WhatsApp Web login (via QR code).
- Searches for a contact.
- Sends a predefined message repeatedly at a custom interval.

## 📋 Prerequisites

Before you run this script, make sure you have the following:

### 🐍 Python
- Python 3.7 or higher

### 📦 Python Packages
Install these with pip:

```bash
pip install selenium
```

### 🌐 Google Chrome
- Make sure you have Google Chrome installed.
- You need the correct version of [ChromeDriver](https://sites.google.com/chromium.org/driver/) that matches your Chrome version.

### 📁 WebDriver
- Download `chromedriver.exe` and place it in the appropriate path on your system.
- Update the `driver_path` in the script to point to your local `chromedriver.exe`.

Example:
```python
driver_path = r"C:\Users\YourUsername\Path\To\chromedriver.exe"
```

## 🚀 How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the script:
   ```bash
   python whatsapp_sender.py
   ```
4. A Chrome browser window will open and load [https://web.whatsapp.com](https://web.whatsapp.com).
5. Scan the QR code using your mobile device.
6. After scanning, the script will find the contact and start sending the message repeatedly at the interval you specified.

## ✏️ Customization

You can modify these variables in the script:

```python
contact_name = "Adam Caine"  # Change to the name of your contact
message = "Answer"           # Message you want to send
interval = 0.5               # Time between each message in seconds
```

## ⚠️ Disclaimer

- This script is for educational purposes only.
- Use responsibly. Spamming may violate WhatsApp's terms of service and get your account restricted or banned.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
