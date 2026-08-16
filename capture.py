import argparse
import json
import os
import uuid
from datetime import datetime
import shutil

RAW_DIR = "raw"
STORAGE_DIR = "storage"

def capture(capture_type, content):
    """
    Captures a piece of information (note, link, or file) and saves it as a structured
    JSON object in the 'raw/' directory.
    """
    # Ensure the raw and storage directories exist
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(STORAGE_DIR, exist_ok=True)

    capture_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    
    source_path = None

    # If the type is a file, copy it to the storage directory
    if capture_type == 'file':
        if not os.path.exists(content):
            print(f"Error: File not found at '{content}'")
            return
        
        # Create a unique filename in storage to avoid conflicts
        _, extension = os.path.splitext(content)
        storage_filename = f"{capture_id}{extension}"
        destination_path = os.path.join(STORAGE_DIR, storage_filename)
        shutil.copy(content, destination_path)
        source_path = destination_path
        print(f"File '{content}' copied to '{destination_path}'")

    data = {
        "id": capture_id,
        "timestamp": timestamp,
        "type": capture_type,
        "content": content if capture_type != 'file' else storage_filename,
        "source_path": source_path
    }

    # Save the JSON object to the raw directory
    filename_ts = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    output_path = os.path.join(RAW_DIR, f"{filename_ts}_{capture_id}.json")
    
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Successfully captured '{capture_type}' with ID {capture_id} to '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture a note, link, or file.")
    parser.add_argument("type", choices=["note", "link", "file"], help="The type of content to capture.")
    parser.add_argument("content", help="The content of the note, the URL of the link, or the path to the file.")
    args = parser.parse_args()
    capture(args.type, args.content)