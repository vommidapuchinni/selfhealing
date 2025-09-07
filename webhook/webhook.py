from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print(data)
    subprocess.call([
        'docker', 'exec', 'ansible'
        'ansible-playbook', '/ansible/restart_nginx.yml'
    ])
    return '', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
