import http.server
import socketserver
import webbrowser
import os
import socket

PORT = 7000
HTML_FILE = "kmap_farm.html"

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#webbrowser.open(f"http://{local_ip}:{PORT}/{HTML_FILE}")
#webbrowser.open(f"http://localhost:7000:{PORT}/{HTML_FILE}")
webbrowser.open(f"http://localhost:{PORT}/{HTML_FILE}")




Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🌐 서버 실행됨: http://{local_ip}:{PORT}/{HTML_FILE}")
    httpd.serve_forever()
