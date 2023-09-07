import os
import json

repo_dir = "./"
index = []

for filename in os.listdir(repo_dir):
    if os.path.isfile(os.path.join(repo_dir, filename)):
        description = input(f"Enter description for {filename}: ")
        index.append({"filename": filename, "description": description})

with open("__index__.json", "w") as f:
    json.dump(index, f, indent=4)
