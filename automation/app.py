from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

SNAPSHOT_DIR = "data/snapshots"
LATEST_FILE = "data/latest.json"


def load_json_file(path):
    with open(path, "r") as file:
        return json.load(file)


def get_snapshots():
    if not os.path.exists(SNAPSHOT_DIR):
        return []

    snapshots = [
        file for file in os.listdir(SNAPSHOT_DIR)
        if file.endswith(".json")
    ]

    return sorted(snapshots, reverse=True)


@app.route("/")
def dashboard():
    snapshots = get_snapshots()
    selected_snapshot = request.args.get("snapshot")

    if selected_snapshot:
        snapshot_path = os.path.join(SNAPSHOT_DIR, selected_snapshot)

        if os.path.exists(snapshot_path):
            data = load_json_file(snapshot_path)
        else:
            data = load_json_file(LATEST_FILE)
            selected_snapshot = "latest"
    else:
        data = load_json_file(LATEST_FILE)
        selected_snapshot = "latest"

    return render_template(
        "index.html",
        data=data,
        snapshots=snapshots,
        selected_snapshot=selected_snapshot
    )


if __name__ == "__main__":
    app.run(debug=True)