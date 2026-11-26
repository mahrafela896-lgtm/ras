import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import bot  # yo import garda bot.py bhitra ko code run huncha

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_web_server():
    port = int(os.environ.get("PORT", 5000))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()

if __name__ == "__main__":
    # Railway ko lagi euta dummy web server background ma chalaune
    threading.Thread(target=run_web_server, daemon=True).start()
    # bot import garda nai chaldai bascha (assuming bot.py ma client.run_until_disconnected() chha)
