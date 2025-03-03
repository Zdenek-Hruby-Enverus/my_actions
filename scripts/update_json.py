import json
import os
from datetime import datetime

FILE_PATH = "data.json"


def update_json_file():
    data = {}

    # Check if file exists
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    # Update timestamp
    data["timestamp"] = datetime.utcnow().isoformat()

    # Write back to file
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    update_json_file()
    print(f"Updated {FILE_PATH} with the latest timestamp.")
