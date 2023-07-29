from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def base():
    return send_from_directory('client/dist/', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('client/dist/', path)

if __name__ == '__main__':
    app.run(debug=True)