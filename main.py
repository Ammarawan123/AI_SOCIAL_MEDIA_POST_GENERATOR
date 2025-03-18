import os
import sys
from text_generator import generate_text
from image_generator import generate_image

# Ensure the generated_content directory exists
IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), "generated_content")
os.makedirs(IMAGE_FOLDER, exist_ok=True)

def main():
    while True:
        try:
            user_input = input("Enter a prompt (or type 'exit' to quit): ").strip()
            if user_input.lower() == "exit":
                print("👋 Goodbye!")
                break

            action = input("Would you like text or image generation? (text/image): ").strip().lower()
            
            if action == "text":
                if callable(generate_text):
                    post_content = generate_text(user_input)
                    print("🤖 Bot:", post_content)
                else:
                    print("❌ Text generation function is not callable.")

            elif action == "image":
                if callable(generate_image):
                    image_filename = generate_image(user_input)
                    if image_filename:
                        image_path = os.path.join(IMAGE_FOLDER, image_filename)
                        print(f"✅ Image saved successfully at {image_path}")
                    else:
                        print("❌ Image generation failed.")
                else:
                    print("❌ Image generation function is not callable.")
            
            else:
                print("⚠️ Invalid choice. Please type 'text' or 'image'.")

        except EOFError:
            print("\n❌ Input error detected. Exiting gracefully...")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        main()
    else:
        print("⚠️ This script is designed to be used interactively. Use 'python main.py run' to start.")