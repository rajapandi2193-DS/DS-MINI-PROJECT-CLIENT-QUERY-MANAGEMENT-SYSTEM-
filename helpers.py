import hashlib
import datetime
import io

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def image_bytes_to_pil(img_bytes):
    try:
        from PIL import Image
        import io
        return Image.open(io.BytesIO(img_bytes))
    except Exception:
        return None
