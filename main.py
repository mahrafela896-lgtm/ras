import os
from flask import Flask
import threading
import bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    if hasattr(bot, 'main'):
        bot.main()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    # port 5000 rakheko chha, 0.0.0.0 ma listen garna parcha
    app.run(host="0.0.0.0", port=5000)
