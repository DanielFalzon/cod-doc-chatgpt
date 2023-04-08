import os

def create_file(content, path):
    directory = os.path.dirname("pages/" + path.lstrip("/"))
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = "pages/" + path.lstrip("/")
    if not path.endswith(".html"):
        filename += "index.html"
    
    with open(filename, "w") as f:
        f.write(content)
    
    print(f"Saved {path} to {filename}")