import flask as fl
from flask import Flask, render_template, request
from PIL import Image
from resizeimage import resizeimage

app = fl.Flask(__name__)

@app.route("/")
def route():
    return app.send_static_file('index.html')

# Adapted from https://www.youtube.com/watch?v=TLgVEBuQURA
@app.route('/upload', methods=['POST'])
def upload():

    filename = secure_filename(file.filename)
    
    with Image.open(file) as image:
        cover = resizeimage.resize_cover(image, [28,28])
        #im.save('img', image.format)
            
    return file.filename
   

if __name__ == "__main__":
    app.run(debug = True)
