from flask import Flask, send_from_directory
from pathlib import Path
import os

YDB_DIR = os.environ.get("YDB_DIR", os.path.join(str(Path.home()), ".ydb"))
ROOT_DIR = os.path.join(os.getcwd(), YDB_DIR)

app = Flask(__name__)


@app.route("/")
def serve_root():
    return serve_dir()


@app.route("/<path:subdir>/")
def serve_dir(subdir=""):
    BASE_DIR = os.path.join(YDB_DIR, subdir)
    entries = os.listdir(BASE_DIR)
    html = "<!doctype html><html><head><title>Directory Listing</title></head><body>"
    html += f"<h1>Directory Listing for {BASE_DIR}</h1><ul>"

    for entry in entries:
        entry_path = os.path.join(BASE_DIR, entry)
        if os.path.isdir(entry_path):
            # Append a trailing slash for directories
            html += f'<li><a href="/{entry}/">{entry}/</a></li>'
        else:
            # Serve files
            html += f'<li><a href="/{subdir}/{entry}">{entry}</a></li>'
    html += "</ul></body></html>"
    return html


@app.route("/<path:folder>/<path:filename>")
def serve_file(folder, filename):
    return send_from_directory(os.path.join(ROOT_DIR, folder), filename)


if __name__ == "__main__":
    app.run(debug=True)
