import cv2
import mediapipe as mp
from cmu_graphics import *
import time

#I watched a tutorial for this part and added comments for me to understand what each line does
mpHands = mp.solutions.hands #hands module for detecting + tracking hands
mpDraw = mp.solutions.drawing_utils #drawing utilities todraw hand landmarks on the image

capture = cv2.VideoCapture(0) #captures from camera 0
capture.set(3, 1280) #width of video frames
capture.set(4, 720) #height of video frames

def main():
    #with runs the code and then if anything breaks it will automatically release the camera and close the window
    with mpHands.Hands(max_num_hands=1, #number of hands to detect
                        min_detection_confidence=0.7, #how confident model needs to be
                        min_tracking_confidence=0.7
    )as hands: #object assigned to hands variable
        while True:
            attempt = 0
            success, img = capture.read() #.read on video capture object and returns boolean if frame was successfully captured and the image itself
            while not success and attempt < 5:
                time.sleep(0.1)  # Wait a bit before trying again
                success, img = capture.read()
                attempt += 1
            if not success:
                print('failed to read frame')
                break
            #sometimes camera feed takes time to load, will try to read frame 5 times before breaking

            img = cv2.flip(img, 1) #mirrors camera
            h, w, _ = img.shape #gets height and width of image (_ is for number of color channels)
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converts image to RGB because openCV uses BGR but mediapipe uses RGB
            result = hands.process(rgb) #processes image to find hands

            if result.multi_hand_landmarks: #if hand landmarks are found
                for hand_landmarks in result.multi_hand_landmarks:
                    mpDraw.draw_landmarks(img, 
                                           hand_landmarks) #draws landmarks and connections on the image
                    fingerTips = {
                        'index': hand_landmarks.landmark[8]
                    }
                    for name, landmark in fingerTips.items():
                        x, y = int(landmark.x * w), int(landmark.y * h) #adjusts landmark to camera
                    
                        cv2.circle(img, (x, y), 10, (255, 0, 255), cv2.FILLED) #draws circle on fingertip
            cv2.imshow("Image", img) #opens window to show image


            if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
                break
            
    capture.release() #stops using webcam
    cv2.destroyAllWindows() #closes all openCV windows


if __name__ == "__main__":
    main()


def onAppStart(app):
    app.width = 1000
    app.height = 1000

def redrawAll(app):
    drawRect(100, 100, 200, 200, fill='red')

def main():
    runApp()

main()