import requests
from io import BytesIO
from coolname import generate_slug
import os
from app import ROOT_DIR

BASE_URL = "http://127.0.0.1:5000"
SESSION_NAME = generate_slug()

def maybe_init_session_page(session_dir):
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)
        index_path = os.path.join(session_dir, "index.html")
        with open(index_path, "a") as f:
            f.write("<!DOCTYPE html>")

def add_text(text):
    session_dir = os.path.join(ROOT_DIR, SESSION_NAME)
    index_path = os.path.join(session_dir, "index.html")
    maybe_init_session_page(session_dir)
    with open(index_path, "a") as f:
        f.write(f"<p>{text}</p>\n")
    return f"Text added to {session_dir}/index.html"


def add_figure(fig):
    buf = BytesIO()
    buf.seek(0)
    
    session_dir = os.path.join(ROOT_DIR, SESSION_NAME)
    maybe_init_session_page(session_dir)

    image_name = generate_slug()
    image_path = os.path.join(session_dir, image_name)
    fig.savefig(image_path, format="png")

    index_path = os.path.join(session_dir, "index.html")
    with open(index_path, "a") as f:
        f.write(f'<p><img src="{image_name}" alt="Image"></p>\n')

    return f"Picture added to {session_dir}/index.html"
