import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
API_KEY = os.getenv("HUGGING_FACE_API_KEY")

def generate_image(prompt):
    if not API_KEY:
        print("🚨 Hugging Face API Key is missing! Set the HUGGING_FACE_API_KEY environment variable.")
        return None

    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200 and "image" in response.headers.get("content-type", ""):
        # Ensure the generated_content directory exists inside the virtual environment
        output_dir = os.path.join(os.path.dirname(__file__), "generated_content")
        os.makedirs(output_dir, exist_ok=True)

        timestamp = int(time.time())
        image_name = f"generated_image_{timestamp}.jpg"
        image_path = os.path.join(output_dir, image_name)
        
        with open(image_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully at {image_path}")
        return image_name  # Return only the image name
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None