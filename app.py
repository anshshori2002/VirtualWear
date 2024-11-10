import os
import requests
import base64
from flask import Flask, render_template, request, jsonify
from PIL import Image
from io import BytesIO

app = Flask(__name__)
api_key = "SG_1afd12a7789c2be8"
url = "https://api.segmind.com/v1/try-on-diffusion"

# Helper function to convert uploaded image files to base64
def image_file_to_base64(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get uploaded images from the request
    model_image = request.files['model_image']
    cloth_image = request.files['cloth_image']

    # Convert images to base64
    model_image_base64 = image_file_to_base64(model_image)
    cloth_image_base64 = image_file_to_base64(cloth_image)

    # Prepare payload for API request
    data = {
        "model_image": model_image_base64,
        "cloth_image": cloth_image_base64,
        "category": "Upper body",
        "num_inference_steps": 35,
        "guidance_scale": 2,
        "seed": 12467,
        "base64": True  # Set to true to get base64 response
    }
    
    headers = {'x-api-key': api_key}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result_base64 = response.json().get('image')  # Get the base64 image
        return jsonify({'image': result_base64})  # Send base64 image as JSON response
    else:
        return jsonify({'error': 'Failed to retrieve image', 'status_code': response.status_code})

if __name__ == '__main__':
    app.run(debug=True)
