from flask import Flask, request, send_from_directory
import os
import base64
from coolname import generate_slug

YDB_DIR = ".ydb"

app = Flask(__name__)
root_dir = os.path.join(os.getcwd(), YDB_DIR)


def maybe_init_session_page(session_dir):
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)
        index_path = os.path.join(session_dir, "index.html")
        with open(index_path, "a") as f:
            f.write("<!DOCTYPE html>")
            f.write("<meta http-equiv='Refresh' content='3'>")


@app.route("/add_text", methods=["POST"])
def add_text():
    session_name = request.form["session_name"]
    text = request.form["text"]
    session_dir = os.path.join(root_dir, session_name)
    index_path = os.path.join(session_dir, "index.html")

    maybe_init_session_page(session_dir)

    with open(index_path, "a") as f:
        f.write(f"<p>{text}</p>\n")

    return f"Text added to {session_dir}/index.html"


@app.route("/add_image", methods=["POST"])
def add_image():
    session_name = request.form["session_name"]

    image_base64 = request.form["image"]
    image_data = base64.b64decode(image_base64)
    image_name = generate_slug()
    session_dir = os.path.join(root_dir, session_name)

    maybe_init_session_page(session_dir)

    image_path = os.path.join(session_dir, image_name)
    with open(image_path, "wb") as img_file:
        img_file.write(image_data)

    index_path = os.path.join(session_dir, "index.html")
    with open(index_path, "a") as f:
        f.write(f'<p><img src="{image_name}" alt="Image"></p>\n')

    return f"Picture added to {session_dir}/index.html"


@app.route("/<path:folder>/<path:filename>")
def serve_file(folder, filename):
    return send_from_directory(os.path.join(root_dir, folder), filename)


if __name__ == "__main__":
    app.run(debug=True)
