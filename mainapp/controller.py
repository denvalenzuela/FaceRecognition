from flask import Flask
from flask_restful import Resource, Api
from mainapp.model import *

class faceDetect(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self,profilename):
        retvalue = upload(profilename)
        return retvalue

class faceRecog(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        retvalue = analyze_img()
        return retvalue

class faceReturn(Resource):
    def get(self,filename):
        retvalue = uploaded_file(filename)
        return retvalue


