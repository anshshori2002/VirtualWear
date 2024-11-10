# VirtualWear

**VirtualWear** is a web-based application that allows users to try on clothing virtually. It enables users to upload an image of themselves and a clothing item, then uses a third-party API to perform a virtual try-on, displaying the clothing item on the user's image.

![screenshot](https://github.com/anshshori2002/VirtualWear/blob/main/Screenshot%20(33).png)
![screenshot](https://github.com/anshshori2002/VirtualWear/blob/main/Screenshot%20(34).png)
![screenshot](https://github.com/anshshori2002/VirtualWear/blob/main/Screenshot%20(35).png)

## Features

- Upload an image of yourself (user image).
- Upload an image of the clothing item you want to try on.
- Preview the images of both the user and the clothing item.
- Get a virtual try-on result showing the clothing item on the user's image.
- Simple and user-friendly interface.

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, JavaScript
- **API**: Segmind API (for clothing try-on feature)
- **Image Handling**: PIL (Python Imaging Library), Base64 encoding
- **Deployment**: Can be deployed on any platform supporting Python.

## Installation

To run the VirtualWear app locally, follow these steps:

### Prerequisites

- Python 3.x
- `pip` (Python package manager)
- An active internet connection for API requests

### Steps to Install

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/virtualwear.git
   cd virtualwear

2. **Set up a virtual environment (optional but recommended)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   
3. **Set up the API key:**

   Create an account with Segmind (or the API provider you're using) and obtain an API key.

5. **Run the Flask app:**
   ```bash
   python app.py
6. **Open your browser and navigate to http://127.0.0.1:5000/ to use the app.**

## Usage

1. **Upload your image**: Use the "Upload User Image" input to upload a photo of yourself.
2. **Upload a clothing item**: Use the "Upload Clothing Image" input to upload an image of the clothing item you want to try on.
3. **Click "Try On"**: After uploading both images, click the "Try On" button. The app will send the images to the backend, where the Segmind API will process them and generate the try-on result.
4. **View the result**: After processing, the result will be displayed on the screen, showing you how the clothing item fits on your image.
