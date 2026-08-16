import pickle
import os
import argparse

def view_pickle_file(filepath):
    """Loads and prints the content of a pickle file."""
    if not os.path.exists(filepath):
        print(f"Error: File not found at '{filepath}'")
        return

    try:
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        
        print(f"--- Contents of '{filepath}' ---")
        print(data)
        print("------------------------------------")

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="View the contents of a .pkl file.")
    parser.add_argument("filepath", help="The path to the .pkl file.", default="data/embeddings.pkl", nargs='?')
    args = parser.parse_args()
    view_pickle_file(args.filepath)