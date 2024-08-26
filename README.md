Here's the README description customized with your repository details:

---

# RTSP Stream to Web Page

This project allows you to stream video from an RTSP source and display it on a web page using Python. The stream parameters such as username, password, IP address, port, and channel can be dynamically entered via the URL.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.6 or later
- `pip` package manager

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/sreesankarp/rtspstream.git
cd rtspstream
```

### Step 2: Create a Virtual Environment (Optional but recommended)

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Required Libraries

Install the necessary Python libraries using `pip`:

```bash
pip install opencv-python flask
```

## Usage

### Step 1: Run the Flask Application

Linux:

```bash
python3 app.py
```

Windows:

```bash
python app.py
```

### Step 2: Access the Stream

Open your web browser and navigate to:

```
http://<your_server_ip>:5000/video_feed?username=your_username&password=your_password&ip=your_ip_address&port=your_port&channel=1&subtype=0
```

Replace the placeholders with your RTSP stream parameters:

- `username`: Your RTSP stream username
- `password`: Your RTSP stream password
- `ip`: IP address of the nvr
- `port`: Port number of the RTSP stream (typically 554)
- `channel`: (Optional) The channel number (default is 1)
- `subtype`: (Optional) The subtype number (default is 0)

### Example URL:

```
http://127.0.0.1:5000/video_feed?username=admin&password=12345&ip=192.168.1.100&port=554&channel=1&subtype=0
```

### Step 3: Full-Screen Video

The video stream will be displayed in full-screen mode within the browser window.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can add this content to your repository's `README.md` file.
