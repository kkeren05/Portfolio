import json
import random
import os


# Load or create database

DATA_FILE = "music_data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {
        "happy": ["Good as Hell - Lizzo", "Happy - Pharrell", "Levitating - Dua Lipa"],
        "sad": ["Someone Like You - Adele", "Jealous - Labrinth", "drivers licence - Olivia Rodrigo"],
        "angry": ["HUMBLE - Kendrick Lamar", "DNA - Kendrick Lamar", "Monster - Kanye West"],
        "chill": ["Sunflower - Post Malone", "Lost in Japan - Shawn Mendes", "Coffee - Beabadoobee"],
        "liked": []
    }


# Ask for mood

mood = input("How are you feeling today? ").lower()

if mood not in data:
    print("I don't know that mood yet, choosing a random song!")
    mood = random.choice(list(data.keys())[:-1])

song = random.choice(data[mood])
print(f"\n🎵 Recommended song: {song}")


# Feedback and learning

feedback = input("\nDid you like this recommendation? (y/n) ").lower()

if feedback == "y":
    data["liked"].append(song)
    print("✅ Saved! Thanks!")
else:
    print("No worries!")


# Save database

with open(DATA_FILE, "w") as f:
    json.dump(data, f, indent=4)

print("\nYour liked songs:", data["liked"])
