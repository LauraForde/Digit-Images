import flask as fl
from flask import Flask, render_template, request

app = fl.Flask(__name__)

@app.route("/")
def route():
    return app.send_static_file('index.html')

# Adapted from https://www.youtube.com/watch?v=TLgVEBuQURA
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['img']
    return file.filename

if __name__ == "__main__":
    app.run(debug = True)