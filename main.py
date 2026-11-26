import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import asyncio

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
    # 1. Pahila web server start gara (Railway le 502 na dekhos bhanera)
    threading.Thread(target=run_web_server, daemon=True).start()
    
    # 2. Ani bot start gara
    import bot
    # client.start() le bot lai connect garcha
    asyncio.run(bot.client.start())
    # run_until_disconnected() le chaldai rakcha
    bot.client.run_until_disconnected()
