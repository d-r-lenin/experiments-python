import cv2
#  create flask app
from flask import Flask, request, jsonify, render_template, redirect, url_for, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/video stream/index.html')

global streaming;
streaming = True

def generate_frames():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0 represents the default camera

    while streaming:
        ret, frame = cap.read()
        if not ret:
            break
        #  encode the frame in JPEG format
        # ret, buffer = cv2.imencode('.jpg', frame)
        # frame_bytes = buffer.tobytes()
        
        
        # object detection
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read the input image
        img = frame
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

        # encode the frame in JPEG format
        ret, buffer = cv2.imencode('.jpg', img)

        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    else:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start')
def start_stream():
    global streaming
    streaming = True
    return "Streaming started"

@app.route('/stop')
def stop_stream():
    global streaming
    streaming = False
    return "Streaming stopped"

#  main function
def main():
    app.run(debug=True, host='localhost', port=5000)

if __name__ == '__main__':
    main()