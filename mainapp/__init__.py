import os
from flask import Flask, render_template
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename

app = Flask(__name__)
application = app
api = Api(app)

# This is the path to the upload directory
# app.config['UPLOAD_FOLDER'] = 'mainapp/uploads/'
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'JPG', 'jpg', 'jpeg', 'gif'])

from mainapp.controller import *

api.add_resource(faceDetect, "/upload/<profilename>")
api.add_resource(faceReturn, "/uploaded/<filename>")
api.add_resource(faceRecog, "/recognize")

@app.route('/')
def index():
  return render_template('index.html')

