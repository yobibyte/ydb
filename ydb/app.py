from flask import Flask, request, send_from_directory
import os

YDB_DIR = ".ydb"
ROOT_DIR = os.path.join(os.getcwd(), YDB_DIR)

app = Flask(__name__)


@app.route("/<path:folder>/<path:filename>")
def serve_file(folder, filename):
    return send_from_directory(os.path.join(ROOT_DIR, folder), filename)


if __name__ == "__main__":
    app.run(debug=True)
