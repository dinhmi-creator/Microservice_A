from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

# Directory containing the images
IMAGE_FOLDER = "images"
image_list = os.listdir(IMAGE_FOLDER)  # Get the list of image files

@app.route('/random_character_image', methods=['GET'])
def random_character_image():
    """Return a random image path."""
    if not image_list:
        return jsonify({"error": "No images available"}), 404
    
    random_image = random.choice(image_list)  # Choose a random image
    image_path = os.path.join(IMAGE_FOLDER, random_image)  # Full path to the image
    
    return jsonify({"image_path": image_path})  # Return as JSON response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
