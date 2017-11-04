import os
from flask import Flask,request, send_file
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from mainapp import app
from mainapp.scripts import main
from mainapp.scripts import train
import numpy as np
import urllib
import cv2

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def upload(profilename):
    # Get the name of the uploaded file
    file = request.files['file']
    # print(file)
    # print(request.files)
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = file.filename
        # Move the file form the temporal folder to
        # the upload folder we setup
        image = grab_image(stream=file)
        # file.save(os.path.join('mainapp/'+app.config['UPLOAD_FOLDER'], filename))
        # print(profilename)
        retval = train.train_img(image,profilename)
        return retval
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        # return send_file(app.config['UPLOAD_FOLDER']+filename,mimetype='image/jpeg')
        # return redirect(url_for('uploaded',filename=filename))

def analyze_img():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        image = grab_image(stream=file)
        retval = main.rec_img(image)
        return retval

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
def uploaded_file(filename):
    return send_file(app.config['UPLOAD_FOLDER']+filename,mimetype='image/jpeg')

def grab_image(path=None, stream=None, url=None):
    # if the path is not None, then load the image from disk
    if path is not None:
        image = cv2.imread(path)
 
    # otherwise, the image does not reside on disk
    else:   
        # if the URL is not None, then download the image
        if url is not None:
            resp = urllib.urlopen(url)
            data = resp.read()
 
        # if the stream is not None, then the image has been uploaded
        elif stream is not None:
            data = stream.read()
 
        # convert the image to a NumPy array and then read it into
        # OpenCV format
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
    # return the image
    return image
