import os
import re

def clean_filenames(folder_path):
    pattern = r"^\d+\.\s"
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print("Wrong folder")
        return

    for filename in os.listdir(folder_path):
        # Search for the pattern in the filename
        new_name = re.sub(pattern, "", filename)

        # If the name changed, rename the file
        if new_name != filename:
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)
            
            try:
                os.rename(old_file, new_file)
                print(f"Renamed: '{filename}' -> '{new_name}'")
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")

folder_path = 'Folder path here'
clean_filenames(folder_path)