from flask import Flask

app = Flask(__name__)

# API endpoint for inference
@app.route('/inference')
def inference():
    return "True"

# API endpoint for health status
@app.route('/health')
def health():
    return "True"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
