def read_text_from_file(filename):
    try:
        with open(filename, 'r') as file:
           
            text = file.read().strip()  
        return text
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None