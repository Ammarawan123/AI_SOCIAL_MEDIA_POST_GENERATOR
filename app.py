from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from text_generator import generate_text
from image_generator import generate_image

app = Flask(__name__)

# Configure the path for the generated_content folder inside the virtual environment
IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), "generated_content")
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

# Ensure the generated_content directory exists
os.makedirs(IMAGE_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt')

        if not prompt:
            return jsonify({"error": "Please provide a prompt."}), 400

        # Generate post content
        post_content = generate_text(prompt) if callable(generate_text) else None
        if not post_content:
            return jsonify({"error": "Post content generation failed."}), 500

        # Generate image
        image_filename = generate_image(prompt) if callable(generate_image) else None
        if not image_filename:
            return jsonify({"error": "Image generation failed."}), 500

        # Generate hashtags and caption
        hashtags = generate_text(f"Generate hashtags for: {prompt}") if callable(generate_text) else ""
        caption = generate_text(f"Generate a caption for: {prompt}") if callable(generate_text) else ""

        # Construct the correct URL for the generated image
        image_url = f"{request.host_url}generated_content/{image_filename}"

        return jsonify({
            "message": "Post generated successfully.",
            "post_content": post_content,
            "hashtags": hashtags,
            "caption": caption,
            "image_url": image_url  # Correctly constructed URL
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generated_content/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['IMAGE_FOLDER'], filename)

@app.route('/favicon.ico')
def favicon():
    return '', 204  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
