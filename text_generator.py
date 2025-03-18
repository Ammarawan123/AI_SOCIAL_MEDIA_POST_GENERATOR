# text_generator.py
import os
import groq
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("\U0001F6A8 GROQ API Key is missing! Set the GROQ_API_KEY environment variable.")

client = groq.Client(api_key=GROQ_API_KEY)

def generate_text(prompt):
    """Generate text response using Groq API"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=256
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"\u274C Error: {e}"

def generate_hashtags(prompt):
    """Generate hashtags using Groq API"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": f"Generate hashtags for: {prompt}"}],
            temperature=0.7,
            max_tokens=64
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"\u274C Error: {e}"

def generate_caption(prompt):
    """Generate caption using Groq API"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": f"Generate a caption for: {prompt}"}],
            temperature=0.7,
            max_tokens=128
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"\u274C Error: {e}"

def generate_description(prompt):
    """Generate description using Groq API"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": f"Generate a description for: {prompt}"}],
            temperature=0.7,
            max_tokens=256
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"\u274C Error: {e}"

def generate_script(prompt):
    """Generate script using Groq API"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": f"Generate a script for: {prompt}"}],
            temperature=0.7,
            max_tokens=512
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"\u274C Error: {e}"