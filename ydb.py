import requests
import base64
from io import BytesIO
from coolname import generate, generate_slug

BASE_URL = "http://127.0.0.1:5000"
SESSION_NAME = generate_slug()


def add_text(text):
    response = requests.post(
        f"{BASE_URL}/add_text", data={"session_name": SESSION_NAME, "text": text}
    )
    return response.text


def add_figure(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    image_base64 = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()

    url = f"{BASE_URL}/add_image"
    data = {
        "session_name": SESSION_NAME,
        "image": image_base64,
    }
    response = requests.post(url, data=data)
    return response.text
