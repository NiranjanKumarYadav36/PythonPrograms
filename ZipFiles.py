import os
import zipfile

# Define your name and roll number
your_name = "Niranjan"
your_roll_no = "65"

# Create directory "<your_name>"
directory_path = your_name
os.makedirs(directory_path, exist_ok=True)

# Create a file named "<Your_roll_no_file1.txt>" and write numbers from 1 to 10 on new lines
file1_path = os.path.join(directory_path, your_roll_no + "_file1.txt")
with open(file1_path, "w") as file1:
    for i in range(1, 11):
        file1.write(str(i) + '\n')

# Create another file named "<Your_roll_no_file2.txt>" and write characters from 'A' to 'Z' on new lines
file2_path = os.path.join(directory_path, your_roll_no + "_file2.txt")
with open(file2_path, "w") as file2:
    for char in range(ord('A'), ord('Z') + 1):
        file2.write(chr(char) + '\n')

# Zip the two files into a zip file named "<Your_roll_no_files.zip>"
zipfile_path = os.path.join(directory_path, your_roll_no + "_files.zip")
with zipfile.ZipFile(zipfile_path, "w") as zip_file:
    zip_file.write(file1_path, os.path.basename(file1_path))
    zip_file.write(file2_path, os.path.basename(file2_path))

print("Files have been created and zipped successfully.")


