import os
import json

repo_dir = "./"
index = []

for filename in os.listdir(repo_dir):
    if os.path.isfile(os.path.join(repo_dir, filename)):
        # Split the filename into name and extension
        name, extension = os.path.splitext(filename)
        index.append({"name": name, "extension": extension})

with open("__index__.json", "w") as f:
    json.dump(index, f, indent=4)
