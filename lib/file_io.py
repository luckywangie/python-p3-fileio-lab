from pathlib import Path

def write_file(file_name, file_content):
    # Convert file_name (PosixPath) to string and add .txt extension
    file_name = str(file_name) + ".txt"
    
    # Open the file in write mode ('w') and write content
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Convert file_name (PosixPath) to string and add .txt extension
    file_name = str(file_name) + ".txt"
    
    # Open the file in append mode ('a') and add content
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    # Convert file_name (PosixPath) to string and add .txt extension
    file_name = str(file_name) + ".txt"
    
    # Open the file in read mode ('r') and return the content
    with open(file_name, 'r') as file:
        return file.read()
