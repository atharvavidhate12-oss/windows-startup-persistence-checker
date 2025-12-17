import json
import hashlib

def calculate_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def load_baseline():
    try:
        with open("baseline.json", "r") as f:
            content = f.read().strip()
            if not content:
                return None
            return json.loads(content)
    except FileNotFoundError:
        return None

def save_baseline(data):
    with open("baseline.json", "w") as f:
        json.dump(data, f, indent=4)
