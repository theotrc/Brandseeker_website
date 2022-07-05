from crypt import methods
import string
import youtube_dl
from requests import request
from App import app
from flask import render_template
import torch
import youtube_dl
import flask
from App import utils
import cv2 as cv
from pathlib import Path 
import sys 
from utils.general import LOGGER, check_file, check_img_size, check_imshow, check_requirements
import requests

sys.path.append('..')



@app.route('/', methods=['get', 'post'])
def accueil():
    
    return render_template("predict.html")



@app.route('/predict', methods=['get', 'post'])
def prediction():
    # model = torch.hub.load('ultralytics/yolov5', 'yolov5m6')
    url = flask.request.form['url']
    data ={'url':url}
    x = requests.post('http://127.0.0.1:5000/predict', json=url, headers={'Content-Type': 'application/json'})
    # utils.dl_yt(str(url))
    return "ok"

@app.route('/testprediction')
def test():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt', force_reload=True)
    stride, names, pt = model.stride, model.names, model.pt
    imgsz = check_img_size((640, 640), s=stride) 
    cam=cv.VideoCapture('Bah ils sont où tes potes -oCVRRHl4NM8.f299.mp4')
    number_of_frame = cam.get(cv.CAP_PROP_FRAME_COUNT)
    print(number_of_frame)
    fps=cam.get(cv.CAP_PROP_FPS)
    print('fps: ', fps)
    n=0
    i=0
    while True:
        ret, frame = cam.read()
        print('first step')
        if (2*n)%fps==0:
            pred = model(frame)
            print('predict in progress')
            i+=1
        n+=1
        if not ret:
            print(i)
            print(n)
            break
    cam.release()
    cv.destroyAllWindows()
    return "okok"