from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

def gen_frames(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)  # Capture the RTSP stream
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    username = request.args.get('username')
    password = request.args.get('password')
    ip = request.args.get('ip')
    port = request.args.get('port')
    channel = request.args.get('channel', '1')  # Default to channel 1
    subtype = request.args.get('subtype', '0')  # Default to subtype 0

    # Construct the RTSP URL based on query parameters
    rtsp_url = f"rtsp://{username}:{password}@{ip}:{port}/cam/realmonitor?channel={channel}&subtype={subtype}"
    
    return Response(gen_frames(rtsp_url), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
