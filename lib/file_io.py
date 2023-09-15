def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f: # Add .txt file extension to the file_name
        f.write(file_content) # Creates a file for content

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content) # Append the content 

def read_file(file_name):
    with open(f'{file_name}.txt') as f:
        return f.read() # Returns the content of the file 