import zipfile
import os
import shutil
from pathlib import Path

# Get the path to the user's desktop
desktop_path = str(Path.home() / "Desktop")

# Define your name
your_name = "Niranjan"

# Define the zip file path
zip_file_name = "65_zip.txt"
zip_file_path = os.path.join(desktop_path, zip_file_name)

# Define the extraction path
extraction_path = os.path.join(your_name)

try:
    # Create the directory "<your_name>"
    os.makedirs(extraction_path, exist_ok=True)

    # Unzip the files into the directory "<your_name>"
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extraction_path)

    # Delete the zip file on the desktop
    os.remove(zip_file_path)

    print("Files have been extracted and zip file has been deleted successfully.")

except Exception as e:
    print("An error occurred:", e)
