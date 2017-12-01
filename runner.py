import flask as flsk
from flask import render_template, request, url_for

app = flsk.Flask(__name__)

@app.route("/")
def route():
    return app.send_static_file('index.html')    

if __name__ == "__main__":
    app.run()