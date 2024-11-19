# Microservice A: Random Character Image Service

## Overview

Microservice A provides a random image path from a pre-defined set of images in the `images/` folder. The service is implemented using Flask and responds to HTTP GET requests. It is designed to demonstrate a simple microservice architecture.

---

## How to Use

### Running the Microservice

1. **Install Python 3.x**: Ensure Python 3.x is installed on your system.

2. **Install Dependencies**:
   ```bash
   pip3 install flask

3. **Navigate to the Microservice Directory**:
   ```bash
   cd microservice_a
   
4. **Start the Microservice**:
   ```bash
   python3 microservice_a.py

The microservice will start and listen at http://127.0.0.1:5000.

## Testing the Microservice

A test program (test_microservice.py) is provided to demonstrate how to interact with the microservice programmatically.

1. **Ensure the microservice is running.**

2. **Run the test program**:
   ```bash
   python3 test_microservice.py

3. **Example Output**:
   ```css
   Calling Microservice A...
   Microservice Response: {'image_path': 'images/image3.jpg'}

## Communication Contact

### Request

Endpoint: http://127.0.0.1:5000/random_character_image
Method: GET
Request Body: None

### Response

Content Type: JSON
Successful Response:
```json
{
    "image_path": "images/image3.jpg"
}
```
Error Response (if no images are available):
```json
{
    "error": "No images available"
}
```

### Programmatic Usage

Requesting Data

Here’s how you can request data programmatically:
```python
import requests

# Define the microservice URL
url = "http://127.0.0.1:5000/random_character_image"

# Send the GET request
response = requests.get(url)

# Handle the response
if response.status_code == 200:
    print(response.json())  # Display the JSON data
else:
    print(f"Error: {response.status_code}")
```

Receiving Data

Here’s how to handle the JSON response programmatically:
```python
# Assuming response is the result of the GET request
if response.status_code == 200:
    data = response.json()
    image_path = data.get("image_path")
    print(f"The image path is: {image_path}")
else:
    print(f"Error: Microservice returned status code {response.status_code}")
```

## UML Sequence Diagram
```plaintext
[Client Program] ---> [Microservice A]: HTTP GET /random_character_image
[Microservice A] ---> [Client Program]: {"image_path": "images/image3.jpg"}
```

## Troubleshooting

1. **No Images Found**:
   Ensure the images/ folder contains valid image files.
   Verify the folder path and permissions.

2. **Microservice Doesn’t Start**:
   Ensure Flask is installed.
   Verify that microservice_a.py is being run from the correct directory.

3. **Connection Errors**:
   Ensure the microservice is running on http://127.0.0.1:5000.
   Check for firewall or network restrictions.

4. **Test Program Errors**:
   Confirm the test program is using the correct endpoint URL.
