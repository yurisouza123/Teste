from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def rastrear():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{now}] IP: {ip}")
    print(f"User-Agent: {user_agent}")
    print("Headers:")
    for header, value in request.headers.items():
        print(f"  {header}: {value}")
    
    return "<h1>Você foi rastreado 😎</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)