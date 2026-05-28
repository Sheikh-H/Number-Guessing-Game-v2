import os
import csv
def save_data(data):
    filename = "scores.csv"
    fieldnames = ["username", "attempts", "time", "won?"]

    # Create file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
        return

    # Load existing scores into memory
    with open(filename, "r", newline="") as f:
        scores = list(csv.DictReader(f))

    # Check if username already exists
    found = False

    for score in scores:
        if score["username"] == data["username"]:
            score["attempts"] = data["attempts"]
            score["time"] = data["time"]
            score["won?"] = data["won?"]
            found = True
            break

    # If username wasn't found, append new entry
    if not found:
        scores.append(data)

    # Rewrite entire file
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scores)