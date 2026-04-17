''' Include a triple-quoted string at the top of 
your code that briefly describes the key features
that you want us to grade. If it is not obvious,
you also need to include brief instructions for 
graders explaining how to make those features visible.
'''
import cv2 as cv
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision

from cmu_graphics import *
print('emily is the best')



def onAppStart(app):
    app.width = 1000
    app.height = 1000

def redrawAll(app):
    drawRect(100, 100, 200, 200, fill='red')

runApp()