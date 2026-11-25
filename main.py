import bot
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# yo class le railway lai app chaldai chha bhanera janauna help garchha (health check)
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive")

def run_web_server():
    port = int(os.environ.get("PORT", 5000))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()

if __name__ == "__main__":
    # web server lai background ma chalaune (railway le khali 404 na dekhos bhanera)
    threading.Thread(target=run_web_server, daemon=True).start()
    
    # timro bot lai chalaune (yadi bot.py ma main() function chha bhane yesari call gara)
    if hasattr(bot, 'main'):
        bot.main()
    else:
        # yadi main() chaina bhane sidhhi bot chaldai chha
        pass
