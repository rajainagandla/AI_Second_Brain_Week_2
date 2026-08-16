import os
import json
from PyPDF2 import PdfReader
import google.genai as genai

def process_capture(content: str, title: str):
    """
    Send content to Gemini AI, capture the output, and store it in captures.json.
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        chat = client.chats.create(model="gemini-1.5-flash")

        response = chat.send_message(content)
        gemini_output = response.text

        capture_entry = {
            "title": title,
            "content": content,
            "gemini_output": gemini_output
        }

        if os.path.exists("captures.json"):
            with open("captures.json", "r", encoding="utf-8") as f:
                captures = json.load(f)
        else:
            captures = []

        captures.append(capture_entry)

        with open("captures.json", "w", encoding="utf-8") as f:
            json.dump(captures, f, indent=4, ensure_ascii=False)

        return gemini_output

    except Exception as e:
        print(f"Error during Gemini analysis: {e}")
        return None


def read_pdf(path: str) -> str:
    """
    Read text from a PDF file and return concatenated content.
    """
    try:
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except FileNotFoundError:
        print(f"PDF file not found: {path}")
        return ""
    except Exception as e:
        print(f"Error reading PDF {path}: {e}")
        return ""
