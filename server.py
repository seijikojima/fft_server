# requests is like axios, request is like req (express)
from flask import Flask, escape, request, jsonify
import requests 
import cv2
import numpy as np
import json

PORT = 5002
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "fft v1.0"

@app.route('/upload', methods=['POST'])
def fft():
    print('Received POST on /upload')

    # signal to spectrum
    data = request.json['data']
    data = np.array(data)
    data = data.astype(float)
    F = np.fft.fft(data)
    print(F.shape)

    # jsonify and response
    return jsonify({"data" : [float(f) for f in F] })

app.run('0.0.0.0',PORT)